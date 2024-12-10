from django.contrib import admin
from .models import Patient, MedicalHistory, PatientProfile

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'contact_number', 'gender', 'date_of_birth')
    search_fields = ('first_name', 'last_name', 'email', 'contact_number')
    list_filter = ('gender', 'date_of_birth')

admin.site.register(MedicalHistory)
admin.site.register(PatientProfile)
