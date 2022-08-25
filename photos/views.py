from django.shortcuts import render, redirect, get_object_or_404

from .models import Photo, Comment
from .forms import CommentForm

# Create your views here.
def home(request):
    photos = Photo.objects.all()
    context = {
        'images': photos
    }
    template = 'index.html'

    return render(request, template, context)

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    template = 'photos/detail.html'

    if request.method == 'POST':
        comment = CommentForm(request.POST or None)

        if comment.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(photo = photo, user = request.user, comment = content)
            comment.save()
            return redirect(photo.get_absolute_url())
    else:
        form = CommentForm()

    context = {
        'photo': photo,
        'form': form,
    }

    return render(request, template, context)