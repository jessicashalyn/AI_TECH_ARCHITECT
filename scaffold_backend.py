import os

def create_file(path, content):
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

FILES = {
    "manage.py": """#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django.") from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
""",
    "requirements.txt": """django==5.1.1
djangorestframework==3.15.2
google-genai==0.3.0
pydantic==2.9.2
gunicorn==23.0.0
whitenoise==6.7.0
dj-database-url==2.2.0
python-dotenv==1.0.1
psycopg2-binary==2.9.9
markdown==3.7
""",
    ".env.example": """SECRET_KEY=django-insecure-example-key
DEBUG=True
ALLOWED_HOSTS=*
DATABASE_URL=sqlite:///db.sqlite3
AI_API_KEY=your_gemini_api_key_here
AI_MODEL=gemini-2.5-flash
""",
    ".env": """SECRET_KEY=django-insecure-example-key-dev-only-change-in-prod
DEBUG=True
ALLOWED_HOSTS=*
DATABASE_URL=sqlite:///db.sqlite3
AI_API_KEY=
AI_MODEL=gemini-2.5-flash
""",
    ".gitignore": """venv/
__pycache__/
*.pyc
db.sqlite3
.env
.DS_Store
static/
""",
    "build.sh": """#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
""",
    "render.yaml": """services:
  - type: web
    name: ai-tech-architect
    env: python
    buildCommand: "./build.sh"
    startCommand: "gunicorn config.wsgi:application"
    envVars:
      - key: PYTHON_VERSION
        value: 3.12.0
      - key: DATABASE_URL
        fromDatabase:
          name: ai_architect_db
          property: connectionString
      - key: SECRET_KEY
        generateValue: true
      - key: AI_API_KEY
        sync: false
      - key: WEB_CONCURRENCY
        value: 4

databases:
  - name: ai_architect_db
    databaseName: ai_architect
    user: ai_architect_user
""",
    "config/__init__.py": "",
    "config/settings.py": """import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-default')
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    
    'rest_framework',
    
    'accounts.apps.AccountsConfig',
    'projects.apps.ProjectsConfig',
    'architecture.apps.ArchitectureConfig',
    'ai_engine.apps.AiEngineConfig',
    'api.apps.ApiConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL', f'sqlite:///{BASE_DIR / "db.sqlite3"}'),
        conn_max_age=600
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'accounts.User'

LOGIN_REDIRECT_URL = 'projects:dashboard'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL = 'accounts:login'

AI_API_KEY = os.environ.get('AI_API_KEY')
AI_MODEL = os.environ.get('AI_MODEL', 'gemini-2.5-flash')
""",
    "config/urls.py": """from django.contrib import admin
from django.urls import path, include
from projects.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('accounts/', include('accounts.urls')),
    path('projects/', include('projects.urls')),
    path('architecture/', include('architecture.urls')),
    path('api/', include('api.urls')),
]
""",
    "config/wsgi.py": """import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
application = get_wsgi_application()
""",
    "config/asgi.py": """import os
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
application = get_asgi_application()
""",
    "accounts/apps.py": """from django.apps import AppConfig
class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
""",
    "accounts/models.py": """from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
""",
    "accounts/admin.py": """from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
admin.site.register(User, UserAdmin)
""",
    "accounts/urls.py": """from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'accounts'
urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
]
""",
    "accounts/views.py": """from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserRegistrationForm

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('projects:dashboard')
        return super().dispatch(request, *args, **kwargs)
""",
    "accounts/forms.py": """from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
""",
    "projects/apps.py": """from django.apps import AppConfig
class ProjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'projects'
""",
    "projects/models.py": """from django.db import models
from django.conf import settings

class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=100, blank=True)
    domain = models.CharField(max_length=100, blank=True)
    stage = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ProjectRequirement(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='requirement')
    app_type = models.CharField(max_length=100, blank=True)
    features = models.TextField(blank=True)
    target_users = models.CharField(max_length=255, blank=True)
    expected_users = models.CharField(max_length=100, blank=True)
    tech_preferences = models.TextField(blank=True)
    infrastructure_requirements = models.TextField(blank=True)
    security_requirements = models.TextField(blank=True)
    scalability_requirements = models.TextField(blank=True)
    additional_requirements = models.TextField(blank=True)

    def __str__(self):
        return f"Requirements for {self.project.name}"
""",
    "projects/admin.py": """from django.contrib import admin
from .models import Project, ProjectRequirement
admin.site.register(Project)
admin.site.register(ProjectRequirement)
""",
    "projects/urls.py": """from django.urls import path
from . import views

app_name = 'projects'
urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('new/', views.ProjectCreateView.as_view(), name='project_create'),
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('<int:pk>/requirements/', views.ProjectRequirementsView.as_view(), name='project_requirements'),
]
""",
    "projects/views.py": """from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project, ProjectRequirement
import json

class HomeView(TemplateView):
    template_name = 'home.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('projects:dashboard')
        return super().dispatch(request, *args, **kwargs)

class DashboardView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'projects/dashboard.html'
    context_object_name = 'projects'
    
    def get_queryset(self):
        return Project.objects.filter(user=self.request.user).order_by('-updated_at')
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from architecture.models import ArchitectureReport
        context['total_projects'] = self.get_queryset().count()
        reports = ArchitectureReport.objects.filter(project__user=self.request.user)
        context['total_reports'] = reports.count()
        context['recent_reports'] = reports.order_by('-created_at')[:5]
        latest_report = reports.order_by('-created_at').first()
        context['latest_score'] = latest_report.architecture_score if latest_report else 0
        return context

class ProjectCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'projects/project_form.html'

class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    
    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)
        
class ProjectRequirementsView(LoginRequiredMixin, View):
    def post(self, request, pk):
        pass # Implementation handled by API
""",
    "architecture/apps.py": """from django.apps import AppConfig
class ArchitectureConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'architecture'
""",
    "architecture/models.py": """from django.db import models
from projects.models import Project

class ArchitectureReport(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='architecture_reports')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    technology_stack = models.JSONField(null=True, blank=True)
    database_design = models.JSONField(null=True, blank=True)
    api_architecture = models.JSONField(null=True, blank=True)
    cloud_architecture = models.JSONField(null=True, blank=True)
    security_checklist = models.JSONField(null=True, blank=True)
    scalability_strategy = models.JSONField(null=True, blank=True)
    diagram_data = models.TextField(null=True, blank=True)
    
    architecture_score = models.IntegerField(null=True, blank=True)
    strengths = models.JSONField(null=True, blank=True)
    risks = models.JSONField(null=True, blank=True)
    improvements = models.JSONField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    
    error_message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Report for {self.project.name} at {self.created_at}"
""",
    "architecture/admin.py": """from django.contrib import admin
from .models import ArchitectureReport
admin.site.register(ArchitectureReport)
""",
    "architecture/urls.py": """from django.urls import path
from . import views

app_name = 'architecture'
urlpatterns = [
    path('report/<int:pk>/', views.ReportDetailView.as_view(), name='report_detail'),
    path('project/<int:project_id>/history/', views.ReportHistoryView.as_view(), name='report_history'),
]
""",
    "architecture/views.py": """from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ArchitectureReport
from projects.models import Project

class ReportDetailView(LoginRequiredMixin, DetailView):
    model = ArchitectureReport
    template_name = 'architecture/report.html'
    context_object_name = 'report'
    
    def get_queryset(self):
        return ArchitectureReport.objects.filter(project__user=self.request.user)

class ReportHistoryView(LoginRequiredMixin, ListView):
    model = ArchitectureReport
    template_name = 'architecture/report_history.html'
    context_object_name = 'reports'
    
    def get_queryset(self):
        self.project = get_object_or_404(Project, pk=self.kwargs['project_id'], user=self.request.user)
        return ArchitectureReport.objects.filter(project=self.project).order_by('-created_at')
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.project
        return context
""",
    "ai_engine/apps.py": """from django.apps import AppConfig
class AiEngineConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ai_engine'
""",
    "ai_engine/schemas.py": """from pydantic import BaseModel, Field
from typing import List, Optional

class TechnologyOption(BaseModel):
    name: str
    description: str
    rationale: str

class DatabaseDesign(BaseModel):
    primary_database: str
    caching_layer: Optional[str]
    description: str
    key_tables_collections: List[str]

class ApiArchitecture(BaseModel):
    style: str
    authentication: str
    description: str
    endpoints_summary: List[str]

class CloudArchitecture(BaseModel):
    provider: str
    compute: str
    storage: str
    description: str

class SecurityItem(BaseModel):
    category: str
    recommendations: List[str]

class ArchitectureResponse(BaseModel):
    technology_stack: List[TechnologyOption]
    database_design: DatabaseDesign
    api_architecture: ApiArchitecture
    cloud_architecture: CloudArchitecture
    security_checklist: List[SecurityItem]
    scalability_strategy: List[str]
    diagram_data: str = Field(description="Mermaid.js diagram syntax")
    architecture_score: int = Field(ge=0, le=100)
    strengths: List[str]
    risks: List[str]
    improvements: List[str]
    summary: str
""",
    "ai_engine/prompts.py": """
SYSTEM_PROMPT = \"\"\"You are an elite Technology Architect AI.
Your task is to analyze project requirements and generate a comprehensive, modern, scalable, and secure technology architecture.

You must reply with ONLY a valid JSON object matching the provided schema. Do not include markdown code blocks around the JSON.
For the diagram_data, use standard mermaid.js syntax (e.g. flowchart TD). Ensure quotes and characters in mermaid are properly escaped.
\"\"\"
""",
    "ai_engine/services.py": """import json
from django.conf import settings
from google import genai
from google.genai import types
from .schemas import ArchitectureResponse
from .prompts import SYSTEM_PROMPT

def generate_architecture_from_requirements(requirements_data: dict) -> dict:
    if not settings.AI_API_KEY:
        raise ValueError("AI_API_KEY is not configured")
        
    client = genai.Client(api_key=settings.AI_API_KEY)
    
    prompt = f"Project Requirements:\\n{json.dumps(requirements_data, indent=2)}\\n\\nGenerate the optimal architecture."
    
    try:
        response = client.models.generate_content(
            model=settings.AI_MODEL,
            contents=[SYSTEM_PROMPT, prompt],
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=ArchitectureResponse,
                temperature=0.2,
            ),
        )
        
        result_json = response.text
        # the response might have markdown block
        if result_json.startswith("```json"):
            result_json = result_json[7:-3]
            
        validated_data = ArchitectureResponse.model_validate_json(result_json)
        return validated_data.model_dump()
    except Exception as e:
        raise Exception(f"AI Generation Failed: {str(e)}")
""",
    "api/apps.py": """from django.apps import AppConfig
class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
""",
    "api/urls.py": """from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('project/create/', views.CreateProjectAPIView.as_view(), name='create_project'),
    path('architecture/generate/<int:project_id>/', views.GenerateArchitectureAPIView.as_view(), name='generate_architecture'),
    path('architecture/status/<int:report_id>/', views.ReportStatusAPIView.as_view(), name='report_status'),
]
""",
    "api/views.py": """from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
import threading

from projects.models import Project, ProjectRequirement
from architecture.models import ArchitectureReport
from ai_engine.services import generate_architecture_from_requirements

class CreateProjectAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        data = request.data
        project = Project.objects.create(
            user=request.user,
            name=data.get('name', 'Untitled Project'),
            description=data.get('description', ''),
            type=data.get('type', ''),
            domain=data.get('domain', '')
        )
        ProjectRequirement.objects.create(
            project=project,
            app_type=data.get('app_type', ''),
            features=data.get('features', ''),
            target_users=data.get('target_users', ''),
            expected_users=data.get('expected_users', ''),
            tech_preferences=data.get('tech_preferences', ''),
            infrastructure_requirements=data.get('infrastructure_requirements', ''),
            security_requirements=data.get('security_requirements', ''),
            scalability_requirements=data.get('scalability_requirements', ''),
            additional_requirements=data.get('additional_requirements', ''),
        )
        return Response({'project_id': project.id}, status=status.HTTP_201_CREATED)

class GenerateArchitectureAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, project_id):
        project = get_object_or_404(Project, id=project_id, user=request.user)
        report = ArchitectureReport.objects.create(project=project, status='processing')
        
        req = project.requirement
        req_data = {
            "name": project.name,
            "description": project.description,
            "app_type": req.app_type,
            "features": req.features,
            "target_users": req.target_users,
            "expected_users": req.expected_users,
            "tech_preferences": req.tech_preferences,
            "infrastructure": req.infrastructure_requirements,
            "security": req.security_requirements,
            "scalability": req.scalability_requirements
        }
        
        def run_ai():
            try:
                result = generate_architecture_from_requirements(req_data)
                report.technology_stack = result.get('technology_stack')
                report.database_design = result.get('database_design')
                report.api_architecture = result.get('api_architecture')
                report.cloud_architecture = result.get('cloud_architecture')
                report.security_checklist = result.get('security_checklist')
                report.scalability_strategy = result.get('scalability_strategy')
                report.diagram_data = result.get('diagram_data')
                report.architecture_score = result.get('architecture_score')
                report.strengths = result.get('strengths')
                report.risks = result.get('risks')
                report.improvements = result.get('improvements')
                report.summary = result.get('summary')
                report.status = 'completed'
                report.save()
            except Exception as e:
                report.status = 'failed'
                report.error_message = str(e)
                report.save()
                
        thread = threading.Thread(target=run_ai)
        thread.start()
        
        return Response({'report_id': report.id}, status=status.HTTP_202_ACCEPTED)

class ReportStatusAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, report_id):
        report = get_object_or_404(ArchitectureReport, id=report_id, project__user=request.user)
        return Response({
            'id': report.id,
            'status': report.status,
            'project_id': report.project.id
        })
"""
}

for filepath, content in FILES.items():
    create_file(filepath, content)
    print(f"Created {filepath}")

print("Done.")
