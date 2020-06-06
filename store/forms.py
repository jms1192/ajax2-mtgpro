from django import forms

class store_register_form(forms.Form):
    store_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    link_store_website = forms.CharField(max_length=300)
    adress = forms.CharField(max_length=200)
    zip_code = forms.CharField(max_length=40)
    blurb_about_store = forms.CharField(widget=forms.Textarea())
    #picture of store 
    username = forms.CharField(max_length=100)
    password_first = forms.CharField(max_length=100)
    password_seccond = forms.CharField(max_length=100)


class event_post(forms.Form):
    event_title = forms.CharField(max_length=100)
    event_date = forms.DateField()
    event_time = forms.CharField(max_length=100)
    event_format = forms.CharField(max_length=100)
    event_discription = forms.CharField(max_length=400, widget=forms.Textarea() )

class promotion_post(forms.Form):
    promotion_title = forms.CharField(max_length=100)
    promotion_discription = forms.CharField(max_length=400, widget=forms.Textarea())
    #way to put in promotion picture 

class change_info(forms.Form):
    store_name = forms.CharField(max_length=100)
    link_store_website = forms.CharField(max_length=300)
    adress = forms.CharField(max_length=200)
    zip_code = forms.CharField(max_length=40)
    blurb_about_store = forms.CharField(widget=forms.Textarea())
    #picture of the store 

class find_store(forms.Form):
    zip_code = forms.CharField(max_length=100)
    distance_in_miles = forms.DecimalField()