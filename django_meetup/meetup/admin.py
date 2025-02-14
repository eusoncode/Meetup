from django.contrib import admin
from .models import Meetup, Location, Participant

# Register your models here.
class ParticipantAdmin(admin.ModelAdmin):
  list_display = ('email',)

class LocationAdmin(admin.ModelAdmin):
  list_display = ('name', 'address')
  list_filter = ('name',)

class MeetupAdmin(admin.ModelAdmin):
  list_display = ('title', 'date', 'location')
  list_filter = ('title', 'location', 'date')
  prepopulated_fields = {'slug':('title',)}


admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Participant, ParticipantAdmin)