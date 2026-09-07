from django.db import models
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
