from django import forms
from . import models


class AddEvent(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = ['title', 'category', 'details', 'venue', 'date', 'time']
