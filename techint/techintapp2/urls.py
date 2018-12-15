from django.urls import path

from . import views

urlpatterns = [
    path('projects', views.projects, name='projects'),
    path('projects/select', views.projects_select, name='projects_select'),
    path('projects/<int:project_id>', views.project_details, name='project_details'),
    path('newDev', views.new_dev, name='new_dev'),
    path('thanks', views.thanks, name='thanks')
]
