from django.urls import path
from . import views

urlpatterns = [
  path('meetup/', views.index, name='all-meetups'), # our-domain.com/meetup
  path('meetup/success', views.confirm_registration, name='confirm-registration'),
  path('meetup/<slug:meetup_slug>', views.meetup_details, name='meetup-detail') # our-domain.com/meetup/<dynamic-path-segment>
]