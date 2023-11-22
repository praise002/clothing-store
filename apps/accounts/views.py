from distutils.log import Log
from django.shortcuts import redirect, render
from django.views import View
from . forms import RegisterForm, LoginForm

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        context = {"form": form}
        return render(request, 'accounts/register.html', context)
    
    def post(self, request):
        return redirect('')
    
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {"form": form}
        return render(request, 'accounts/login.html', context)
    
    def post(self, request):
        return redirect('')
    
