from django.shortcuts import render, redirect
from datetime import date
from .models import Post, User
from .forms import SignUpForm

# Create your views here.


def home(request):
    if request.method == 'GET':
        SignUp = SignUpForm()
    else:
        SignUp = SignUpForm(request.POST)
        if SignUp.is_valid():
            user_email = SignUp.cleaned_data['email']
            user, was_created = User.objects.get_or_create(email=user_email)
            return redirect('confirm_signup')

    return render(request, "home/home.html",{
        'form': SignUp
    })


def post(request):
    allPosts = Post.objects.all()
    return render(request, "home/all-post.html", {"posts": allPosts})


def post_detail(request, post_slug):
    clicked_post = Post.objects.get(slug=post_slug)
    return render(request, "home/post-detail.html", {"post": clicked_post})


def confirm_signup(request):
    return render(request, 'home/SignUp_Confirmation.html')



