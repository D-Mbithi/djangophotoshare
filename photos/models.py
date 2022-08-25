from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
class Photo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('photos:photo_detail', kwargs={'pk': self.pk})


class Like(models.Model):
    pass


class Comment(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    written_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.written_at)
    