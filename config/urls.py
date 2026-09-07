from django.contrib import admin
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
