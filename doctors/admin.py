from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialty', 'email', 'contact_number')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('specialty',)
