from django import forms

#tye in another users name here to follow
class follow_form(forms.Form):
    follow = forms.CharField(widget=forms.TextInput)

class follow_store_form(forms.Form):
    store_name = forms.CharField(widget=forms.TextInput) 