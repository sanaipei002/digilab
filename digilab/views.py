# digilab/views.py
from django.views.generic import TemplateView

class DashboardView(TemplateView):
    template_name = 'digilab/dashboard.html' 
