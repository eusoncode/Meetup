from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetup

# Create your views here.

def index(request):
    """
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
    
    """
    meetups = Meetup.objects.all()
    return render(request, 'meetup/index.html', {
        'meetups': meetups,
    })

def meetup_details(request, meetup_slug):
    """
        selected_meetup = {
            'title': 'A First Meetup',
            'description': 'This is my first meetup in Edmonton soutwest'
        }
    """
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        return render(request, 'meetup/meetup-details.html', {
            'meetup_found': True,
            'meetup': selected_meetup
        } )
    except Exception as exc:
        return render(request, 'meetup/meetup-details.html', {
            'meetup_found': False
        })