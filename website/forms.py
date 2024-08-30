from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email=forms.EmailField(label="Email Address",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'abc@email.com'}))
    first_name=forms.CharField(label="FIrst Name",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Abc'}))
    last_name=forms.CharField(label="Last Name",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Defg'}))
    dob = forms.DateField(label="Date of Birth",widget=forms.DateInput(attrs={'class': 'form-control','placeholder': 'YYYY-MM-DD','type': 'date' }))
    
    class Meta:
        model = User
        fields = ('first_name','last_name','email','dob','username','password1','password2')

    def __init__(self, *args: Any, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = 'UserName'
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Set Password'
        self.fields['password1'].label = 'Password'
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
     