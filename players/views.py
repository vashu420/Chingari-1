from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from rest_framework.views import APIView
from .models import *
from django.http import FileResponse, HttpResponse,  HttpResponseRedirect, HttpRequest
from rest_framework.response import Response
from rest_framework import generics, mixins, permissions, status



# Create your views here.

class RegisterLoginView(LoginView):
    template_name = 'players/login.html'

def login_page(request):
    return render(request, 'login.html')


class SaveLoginDetails(APIView):
    def post(self,request):
        if request.method == "POST":
            username=request.POST['loginName']
            loginPhoneNumber=request.POST['loginPhoneNumber']
            print('username',username)
            print('loginPhoneNumber',loginPhoneNumber)
            RegisterUser.objects.create(identity =username, mobile_number =loginPhoneNumber, whatsapp_number =loginPhoneNumber)
            return Response({'message' : 'All Saved!'}, status = status.HTTP_200_OK)
            
