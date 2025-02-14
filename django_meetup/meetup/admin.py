from django.contrib import admin
from .models import Meetup, Location

# Register your models here.


class LocationAdmin(admin.ModelAdmin):
  list_display = ('name', 'address')
  list_filter = ('name',)

class MeetupAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug', 'description')
  list_filter = ('title',)
  prepopulated_fields = {'slug':('title',)}


admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location, LocationAdmin)