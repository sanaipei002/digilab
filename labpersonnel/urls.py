# labpersonnel/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.LabPersonnelDashboardView.as_view(), name='labpersonnel_dashboard'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('completed-tests/', views.CompletedTestView.as_view(), name='completed_tests'),
    path('ongoing-tests/', views.OngoingTestView.as_view(), name='ongoing_tests'),
    path('update-test/<int:pk>/', views.UpdateTestView.as_view(), name='update_test'),
    path('broadcasted-request/', views.BroadcastedRequestView.as_view(), name='broadcasted_request'),
    path('sidebar/', views.SidebarView.as_view(), name='sidebar'),
    path('request-payment/', views.RequestPaymentView.as_view(), name='request_payment'),
]
