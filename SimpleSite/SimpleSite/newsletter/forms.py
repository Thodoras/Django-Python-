from django import forms

from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    def clean_email(self):
    	email = self.cleaned_data.get('email')
    	base, provider = email.split("@")
    	domain, extension = provider.split(".")
    	if "edu" != extension:
    		raise forms.ValidationError("Please use a valid edu address.")
    	return email
