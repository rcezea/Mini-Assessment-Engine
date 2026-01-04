from django.urls import path
from .views import (
    ExamListAPIView,
    ExamDetailAPIView,
)


urlpatterns = [
    path("exams/", ExamListAPIView.as_view()),
    path("exams/<int:exam_id>/", ExamDetailAPIView.as_view()),
]
