from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from rest_framework.views import APIView


# Create your views here.

class RegisterLoginView(LoginView):
    template_name = 'players/login.html'

def login_page(request):
    return render(request, 'login.html')


class SaveLoginDetails(APIView):
    def post(request):
        if request.method == "POST":
            username=request.POST['loginName']
            loginPhoneNumber=request.POST['loginPhoneNumber']
            print('username')
            print('loginPhoneNumber')
            pass
