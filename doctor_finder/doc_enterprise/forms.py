from django import forms

class DoctorRegister(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    mobile = forms.IntegerField()
    profile_pic = forms.FileField()
