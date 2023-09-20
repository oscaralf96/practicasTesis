from django.contrib.auth import views as auth_views

class LoginView(auth_views.LoginView):
    """Login view."""

    template_name = 'users/login.html'
