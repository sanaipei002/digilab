# patients/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.PatientDashboardView.as_view(), name='patient_dashboard'),
    path('test-available/', views.TestAvailableView.as_view(), name='test-available'),
    path('test-results/', views.TestResultsView.as_view(), name='test-results'),
    path('request-new-test/', views.RequestNewTestView.as_view(), name='request-new-test'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('payment/', views.PaymentView.as_view(), name='payment'),
    path('medical-history/', views.MedicalHistoryView.as_view(), name='medical-history'),
    path('sidebar/', views.PatientSidebarView.as_view(), name='patient-sidebar'),
]
