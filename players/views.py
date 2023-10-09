from django.shortcuts import render
from django.contrib.auth.views import LoginView

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Replace 'home' with your desired redirect URL
    else:
        form = CustomUserRegistrationForm()
    
    return render(request, 'your_app_name/register.html', {'form': form})


class RegisterLoginView(LoginView):
    template_name = 'players/login.html'

