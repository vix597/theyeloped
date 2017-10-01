from django.http import HttpResponse
from django.template import loader
from .models import Rsvp, RsvpForm

def is_invited(first_name, last_name):
    '''
    Get all the entries in the leaderboard
    '''

    if first_name is None or last_name is None:
        return {'invited': False, "error": "No name provided"}

    # Normalize input
    first_name = first_name.strip().lower()
    last_name = last_name.strip().lower()

    try:
        #pylint: disable=E1101
        ret = Rsvp.objects.filter(first_name__iexact=first_name, last_name__iexact=last_name)
        if len(ret) == 0:
            return {"invited": False, "error": "No person matches the query"}
        elif len(ret) > 1:
            return {"invited": False, "error": "More than one person matches the query"}
        else:
            return {"invited": True, "rsvp": ret[0]}
    except BaseException as e:
        return {'invited': False, "error": str(e)}

def index(request):
    template = loader.get_template('elopement/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def search_invitees(request):
    print("SEARCH INVITEES")
    context = {}
    if request.POST:
        d = request.POST.dict()
        print("Search invitees: ", d)
        first_name = d.get("first_name", None)
        last_name = d.get("last_name", None)
        context = is_invited(first_name, last_name)
        print("Context: ", context)

    template = loader.get_template("elopement/rsvp.html")
    return HttpResponse(template.render(context, request))

def rsvp(request):
    context = {}
    if request.POST:
        d = request.POST.dict()
        print("RSVP: ", d)
        res = is_invited(d.get("first_name", None), d.get("last_name", None))
        if res.get("invited", False) and res.get("rsvp", None) is not None:
            try:
                form = RsvpForm(request.POST, instance=res["rsvp"])
                form.save() # Forcing update prevents inserting a new entry
                context = {"rsvp_success": True}
            except BaseException as e:
                print("Error creating form from post data: ", str(e))
                print("Post data: ", request.POST)
                context = {"rsvp_success": False, "error": str(e)}

    template = loader.get_template('elopement/rsvp.html')
    return HttpResponse(template.render(context, request))
