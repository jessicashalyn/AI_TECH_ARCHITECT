from django.db import models
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
