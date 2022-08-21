from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import signup, profile

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]