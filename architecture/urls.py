from django.urls import path
from . import views

app_name = 'architecture'
urlpatterns = [
    path('report/<int:pk>/', views.ReportDetailView.as_view(), name='report_detail'),
    path('project/<int:project_id>/history/', views.ReportHistoryView.as_view(), name='report_history'),
]
