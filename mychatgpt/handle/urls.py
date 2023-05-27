from django.urls import path
from . import views

urlpatterns = [
     path('', views.question_view.as_view(), name='home'),
]
