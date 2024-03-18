from django.urls import path
from players.views import *
from . import views



urlpatterns = [
    path('', login_page, name='login'),
    path('login/', RegisterLoginView.as_view(), name='login'),
    path('save_login_details/', SaveLoginDetails.as_view(), name='save_login_details'),

    # path('login/', views.user_login, name='login'),
    # path('signup/', views.user_signup, name='signup'),
    # path('logout/', views.user_logout, name='logout'),

    
]