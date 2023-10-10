from django.urls import path
from players.views import *

urlpatterns = [
    path('', login_page, name='login'),
    path('login/', RegisterLoginView.as_view(), name='login'),
    path('save_login_details/', SaveLoginDetails.as_view(), name='save_login_details'),

    
]