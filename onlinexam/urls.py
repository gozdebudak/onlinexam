from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/5/
    path('exam/<int:exam_id>/solve', views.detail, name='detail'),
    path('exam/<int:exam_id>/notStarted', views.notStarted, name='notStarted'),
    path('exam/<int:exam_id>/expired', views.expired, name='expired'),
]