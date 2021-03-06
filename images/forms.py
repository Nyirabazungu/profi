from .models import Profile,Image,Comments
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        email = forms.EmailField(label='Email')
        model = Profile
        exclude = ['user']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','profile']

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user']

