from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('project/create/', views.CreateProjectAPIView.as_view(), name='create_project'),
    path('architecture/generate/<int:project_id>/', views.GenerateArchitectureAPIView.as_view(), name='generate_architecture'),
    path('architecture/status/<int:report_id>/', views.ReportStatusAPIView.as_view(), name='report_status'),
]
