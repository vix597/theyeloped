from django.shortcuts import redirect

def index(_): #Passing _ variable to avoid linting warning
    return redirect("/elopement/", permanent=True)
