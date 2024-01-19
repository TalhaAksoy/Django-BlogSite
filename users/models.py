from django.db import models
from django.forms import PasswordInput

class UserProfile(models.Model):
    username = models.CharField(max_length=20, default='', blank=False)
    password = models.CharField(max_length=20, default='', blank=False)
    email = models.EmailField(max_length=100, default='', blank=False)

    # isimler forms.pydakiyle ayni olurse inputlarindan ozellik ekleyebiliyoruz
