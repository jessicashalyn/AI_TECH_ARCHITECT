from django.shortcuts import render, get_object_or_404
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
