from django.urls import path
from players.views import RegisterLoginView

urlpatterns = [
    path('login/', RegisterLoginView.as_view(), name='login'),
]