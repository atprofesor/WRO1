from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dance/<str:dance_name>/<str:stage>/', views.dance_stage, name='dance_stage'),
]
