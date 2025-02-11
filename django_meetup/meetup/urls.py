from django.urls import path
from . import views

urlpatterns = [
  path('meetup/', views.index), # our-domain.com/meetup
  path('meetup/<slug:meetup_slug>', views.meetup_details) # our-domain.com/meetup/<dynamic-path-segment>
]