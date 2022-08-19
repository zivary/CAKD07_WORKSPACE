from django.urls import path
from . import views

urlpatterns = [
    path('', views.program_inputdata, name="program_inputdata"),
    path('program_result/', views.program_result, name="program_result"),
]