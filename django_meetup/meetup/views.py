from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    meetups = [
        {
            'title': 'A First Meetup',
            'location': 'Edmonton soutwest',
            'slug': 'a-first-meetup'
        },
        {
            'title': 'A Second Meetup',
            'location': 'Edmonton northwest',
            'slug': 'a-second-meetup'
        }
    ]
    return render(request, 'meetup/index.html', {
        'meetups': meetups,
        'show_meetups': True
    })