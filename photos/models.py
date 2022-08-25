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
    likes = models.ManyToManyField(User, related_name='blogpost_like')


    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photos:photo_detail', kwargs={'pk': self.pk})


class Like(models.Model):
    pass


class Comment(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    written_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['written_at']

    def __str__(self):
        return str(self.written_at)
    