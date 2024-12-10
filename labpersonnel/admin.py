from django.contrib import admin
from .models import LabPersonnel

@admin.register(LabPersonnel)
class LabPersonnelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'email', 'contact_number')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('position',)
