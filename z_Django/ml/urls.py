from django.urls import path
from . import views

urlpatterns = [
    path('', views.ml_inputdata, name="ml_inputdata"),
    path('ml_result/', views.ml_result, name="ml_result"),
]