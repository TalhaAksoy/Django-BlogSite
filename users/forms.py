from django import forms
from . import models

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class" : "border-[1px] pl-2 py-4 w-full rounded-md", "placeholder" : "Write Password"}), label="")
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class" : "border-[1px] pl-2 py-4 w-full rounded-md", "placeholder" : "Write Email"}), label="")
    username = forms.CharField(widget=forms.TextInput(attrs={"class" : "border-[1px] pl-2 py-4 w-full rounded-md", "placeholder" : "Write Username"}), label="")
    #isimler models.pydakiyle ayni olmali ki eslessinler
    class Meta:
        model = models.UserProfile
        exclude = ("user",)