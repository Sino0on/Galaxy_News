from django.shortcuts import render
from user.models import Post
# Create your views here.


def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


# def show_img(request, Y, m, d, name):
#     return render(request, f'media/Photos/{Y}/{m}/{d}/{name}.png')
