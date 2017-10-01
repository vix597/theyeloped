from django.db import models
from django.forms import ModelForm

class Rsvp(models.Model):
    '''
    Database model for an RSVP entry
    '''
    #: First name of invitee
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    #: Last name of invitee
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    #: Are they attending?
    attending = models.BooleanField(default=False)

    #: Allergies
    allergies = models.CharField(max_length=1000, blank=True, verbose_name="Allergies")
    #: Names of people attending (JSON obj)
    names = models.CharField(max_length=5000, blank=True, verbose_name="Additional Guests")
    #: Favorite song
    favorite_song = models.CharField(max_length=100, blank=True, verbose_name="Favorite Song")
    #: Note for the bride & groom
    note = models.CharField(max_length=10000, blank=True, verbose_name="Note to the Bride & Groom")

    #: Internal - When they were invited
    invited_date = models.DateTimeField(auto_now_add=True)
    #: Internal - When they responded
    response_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        att = "not attending"
        if self.attending:
            att = "attending"

        return "{} {} is {}".format(self.first_name, self.last_name, att)

class RsvpForm(ModelForm):
    '''
    Handles post data to update the RSVP list
    '''
    class Meta:
        model = Rsvp
        fields = [
            'first_name', 'last_name', 'attending',
            'allergies', 'names', 'favorite_song',
            'note'
        ]
