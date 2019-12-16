from django.http import Http404
from django.shortcuts import render, redirect
from .models import User

def home(request):
    return render(request, 'home.html')


def verify(request, uuid):
    try:
        user = User.objects.get(verification_uuid=uuid, is_verified=False)
    except User.DoesNotExist:
        raise Http404("User does not exist or is already verified")

    user.is_verified = True
    user.save()

    return redirect('home')

def view_post(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404("Poll does not exist")

    post.view_count += 1
    post.save()

    return render(request, 'post.html', context={'post': post})
