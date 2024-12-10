# labpersonnel/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
#from .models import Test  # Import your models if needed


class LabPersonnelDashboardView(TemplateView):
    template_name = 'labpersonnel/dashboard.html' 
    
class ProfileView(TemplateView):
    template_name = 'labpersonnel/profile.html'

class CompletedTestView(TemplateView):
    template_name = 'labpersonnel/completed-test.html'

class OngoingTestView(TemplateView):
    template_name = 'labpersonnel/ongoing-test.html'

class UpdateTestView(TemplateView):
    template_name = 'labpersonnel/update-test.html'

    # If you want to handle form submissions or object retrieval, you can override get_context_data or form_valid
   # def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
       # test_id = self.kwargs.get('pk')
        #context['test'] = Test.objects.get(id=test_id)  # Example: fetching a test by its ID
        #return context

class BroadcastedRequestView(TemplateView):
    template_name = 'labpersonnel/broadcasted-request.html'

class SidebarView(TemplateView):
    template_name = 'labpersonnel/sidebar.html'

class RequestPaymentView(TemplateView):
    template_name = 'labpersonnel/request-payment.html'
