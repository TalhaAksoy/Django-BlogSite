from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from . import forms


# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('')

def register_page(request):
    form = forms.UserRegisterForm
    if request.method == "POST":
        print(request.POST)
        user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
        user.save()
        if user is not None:
            return redirect('login')
    return render(request, "users/register.html", {"form" : form})
