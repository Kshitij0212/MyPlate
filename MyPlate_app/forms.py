from django import forms
from django.forms.widgets import HiddenInput

class PreRecordForm(forms.Form):
    totalCalories = forms.DecimalField(max_digits=10, decimal_places=2, widget=HiddenInput, initial={} )
    cc_myself = forms.BooleanField(required=False)