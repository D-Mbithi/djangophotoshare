from django.urls import path
from .views import photo_detail


app_name = 'photos'


urlpatterns = [
    path('photo/<int:pk>', photo_detail, name="photo_detail"),
]