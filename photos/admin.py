from django.contrib import admin
from .models import Photo, Comment, Like


# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded_at']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass