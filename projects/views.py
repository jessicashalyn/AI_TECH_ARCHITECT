from django.shortcuts import render, redirect, get_object_or_404
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
