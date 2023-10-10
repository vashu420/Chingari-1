from django.shortcuts import render
from django.contrib.auth.views import LoginView

# Create your views here.

class RegisterLoginView(LoginView):
    template_name = 'players/login.html'

def login_page(request):
    return render(request, 'login.html')