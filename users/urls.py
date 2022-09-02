from re import template
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import signup, profile, activate

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('activate/<uidb64>/<token>', activate, name="activate"),
]