from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path('success/', views.confirm_signup, name='confirm_signup'),
    path("posts/", views.post, name="allpost"),
    path("posts/<slug:post_slug>", views.post_detail, name="post_details"),
    
]
