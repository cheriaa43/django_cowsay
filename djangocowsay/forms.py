from django import forms


class SpeakForm(forms.Form):
    text = forms.CharField(max_length=80)
