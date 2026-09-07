from rest_framework.views import APIView
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
