from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound
from datetime import date

allPosts = [
    {
        "slug": "dog-halloween",
        "image": "halloweendog.jpg",
        "author": "Ralph",
        "date": date(2022, 1, 28),
        "title": "Whats safe for dogs to eat on halloween",
        "excerpt": "Something to read so you and your dog can have a great halloween",
        "content": """
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod aqtempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod aqtempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod aqtempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
        """
    },
    {
        "slug": "sick-dog",
        "image": "sickdog.jpg",
        "author": "Ralph",
        "date": date(2021, 4, 29),
        "title": "How to care for a sick dog",
        "excerpt": "Your Fur baby is sick lets see if we can help",
        "content": """
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod aqtempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod aqtempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod aqtempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
        """
    },
    {
        "slug": "dog-vacations",
        "image": "dogbeach.jpg",
        "author": "Ralph",
        "date": date(2019, 7, 2),
        "title": "Best Dog Vacation Locations",
        "excerpt": "In this post we will share with you the hottest vacation spots you and your pooch will love",
        "content": """
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod aqtempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod aqtempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod aqtempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
        """
    },
]


def get_date(post):
    return post['date']
# Create your views here.


def home(request):
    sorted_posts = sorted(allPosts, key=get_date)
    latest_post = sorted_posts[-3:]
    return render(request, "home/home.html", {
        "posts": latest_post
    })


def post(request):
    return render(request, "home/all-post.html", {"posts": allPosts})


def post_detail(request, slug):
    clicked_post = next(post for post in allPosts if post['slug'] == slug)
    return render(request, "home/post-detail.html",{
        "posts": clicked_post
    })


