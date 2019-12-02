from django import forms
from . import views

class uploadform(forms.Form):
	file = forms.FileField()
