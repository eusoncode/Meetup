from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetup
from .forms import RegistrationForm

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
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                participant = registration_form.save()
                selected_meetup.participant.add(participant)
        
        return render(request, 'meetup/meetup-details.html', {
            'meetup_found': True,
            'meetup': selected_meetup,
            'form': registration_form
        } )
    except Exception as exc:
        return render(request, 'meetup/meetup-details.html', {
            'meetup_found': False
        })