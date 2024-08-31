from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Customer
class SignUpForm(UserCreationForm):
    email=forms.EmailField(label="Email Address",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'abc123@email.com'}))
    first_name=forms.CharField(label="FIrst Name",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'John'}))
    last_name=forms.CharField(label="Last Name",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Doe'}))
    dob = forms.DateField(label="Date of Birth",widget=forms.DateInput(attrs={'class': 'form-control','placeholder': 'YYYY-MM-DD','type': 'date' }))
    usable_password = None
    class Meta:
        model = User
        fields = ('first_name','last_name','dob','email','username','password1','password2')

    def __init__(self, *args: Any, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = 'Username'
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Set Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

#Create a form to add a record
class Add_customer_form(forms.ModelForm):
    first_name=forms.CharField(required=True,label="First Name",widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'John'}))
    last_name=forms.CharField(required=True,label="Last Name",widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'Doe'}))
    email= email = forms.EmailField(required=True,label="Email Address",widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'john.doe@example.com'}))
    date_of_birth=date_of_birth = forms.DateField(required=True,label="Date of Birth",widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}))
    address=forms.CharField(required=True,label="Address",widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'Permanent Address'}))
    phone=forms.CharField(required=True,label="Phone Number",widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'0123456789'}))
    city=forms.CharField(required=True,label="City",widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'Bengaluru'}))
    state=forms.CharField(required=True,label="State",widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'Karnataka'}))
    pincode=forms.CharField(required=True,label="Pincode",widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'123456'}))

    class Meta:
        model = Customer
        exclude = ("user",)
