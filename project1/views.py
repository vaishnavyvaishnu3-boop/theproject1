from django.shortcuts import render


def home(request):
    posts = [
        {
            "title": "First Blog Post",
            "content": "This is my first django blog post."
        },
        {
            "title": "Learning django",
            "content": "Django makes web development easy."
        },
        {
            "title": "Templates in django",
            "content": "Django templates helps separate logic and html."
        }
    ]
    return render(request, 'home.html', {"posts": posts})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')

# Create your views here.
