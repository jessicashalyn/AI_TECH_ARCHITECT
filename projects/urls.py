from django.urls import path
from . import views

app_name = 'projects'
urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('new/', views.ProjectCreateView.as_view(), name='project_create'),
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('<int:pk>/requirements/', views.ProjectRequirementsView.as_view(), name='project_requirements'),
]
