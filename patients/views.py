# patients/views.py

from django.shortcuts import render
from django.views.generic import TemplateView

class PatientDashboardView(TemplateView):
    template_name = 'patients/dashboard.html'

class TestAvailableView(TemplateView):
    template_name = 'patients/test-available.html'

class TestResultsView(TemplateView):
    template_name = 'patients/test-results.html'

class RequestNewTestView(TemplateView):
    template_name = 'patients/request-new-test.html'

class ProfileView(TemplateView):
    template_name = 'patients/profile.html'

class PaymentView(TemplateView):
    template_name = 'patients/payment.html'

class MedicalHistoryView(TemplateView):
    template_name = 'patients/medical-history.html'

class PatientSidebarView(TemplateView):
    template_name = 'patients/patient-sidebar.html'
