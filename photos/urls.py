from django.urls import path
from .views import photo_detail, photo_upload, photo_likes


app_name = 'photos'


urlpatterns = [
    path('photo/<int:pk>', photo_detail, name="photo_detail"),
    path('photo/upload', photo_upload, name="photo_upload"),
    path('likes/<int:pk>',photo_likes, name='photo_likes' )
]