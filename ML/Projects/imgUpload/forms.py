from django import forms

class imageUploadform(forms.Form):
    image = forms.ImageField()