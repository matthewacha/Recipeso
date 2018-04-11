from django import forms

class UserRegister(forms.Form):
    email=forms.CharField(max_length=40,
                          widget=forms.TextInput(attrs={'class':'form-input',
                                                        'placeholder':'your@email.com',
                                                        'required': True}))
    password=forms.CharField(max_length=100,
                             widget=forms.TextInput(attrs={'class':'form-input',
                                                        'placeholder':'*********',
                                                        'required': True}))
