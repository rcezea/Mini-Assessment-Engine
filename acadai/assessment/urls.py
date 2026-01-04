from django.urls import path
from .views import (
    ExamListAPIView,
    ExamDetailAPIView,
    SubmitExamAPIView,
)


urlpatterns = [
    path("exams/", ExamListAPIView.as_view()),
    path("exams/<int:exam_id>/", ExamDetailAPIView.as_view()),
    path("exams/<int:exam_id>/submit/", SubmitExamAPIView.as_view()),

]
