from django.urls import path
from players.views import *

urlpatterns = [
    path('', login_page, name='login'),
    path('login/', RegisterLoginView.as_view(), name='login'),
]