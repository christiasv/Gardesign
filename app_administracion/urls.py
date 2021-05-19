from django.urls import path, include

from app_website.views import HomeView

app_name = 'app_administracion'

urlpatterns = [
    path('api/', include('app_administracion.api.urls', namespace='api')),
]