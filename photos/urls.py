from django.urls import path
from .views import photo_detail, photo_upload


app_name = 'photos'


urlpatterns = [
    path('photo/<int:pk>', photo_detail, name="photo_detail"),
    path('photo/upload', photo_upload, name="photo_upload"),

]