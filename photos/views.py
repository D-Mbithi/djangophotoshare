from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Photo, Comment
from .forms import CommentForm, PhotoForm

# Create your views here.
def home(request):
    photos = Photo.objects.all()
    
    # if request.user:
        # count = Photo.objects.all().filter(owner=request.user).count()
    count = 0 
    
    
    context = {
        'images': photos,
        'count': count,
    }
    template = 'index.html'

    return render(request, template, context)

@login_required
def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    template = 'photos/detail.html'

    likes = photo.total_likes()

    if request.method == 'POST':
        comment = CommentForm(request.POST or None)

        if comment.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(photo=photo, author=request.user, comment=content)
            comment.save()
            return redirect(photo.get_absolute_url())
    else:
        form = CommentForm()

    context = {
        'photo': photo,
        'form': form,
        'likes': likes,

    }

    return render(request, template, context)


@login_required
def photo_upload(request):

    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            user = request.user
            image = request.FILES.get('photo')
            title = request.POST.get('title')
            description = request.POST.get('description')

            photo  = Photo.objects.create(owner=user, title=title, photo=image, description=description)
            photo.save()
            messages.success(request, 'Your image was uploaded successfully!')
            
            return redirect('/')
    else:
        form = PhotoForm()

    context = {
        'form': form
    }

    template = 'photos/upload.html'

    return render(request, template, context)


@login_required
def photo_likes(request, pk):
    photo = get_object_or_404(Photo, pk=request.POST.get('photo_id'))
    photo.likes.add(request.user)
    
    return HttpResponseRedirect(reverse('photos:photo_detail', args=[str(pk)]))