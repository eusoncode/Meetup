from django import forms
# from .models import Participant

# Switching back to Form model
class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Your email')

"""
# This was the Form model initially use

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['email']    
"""