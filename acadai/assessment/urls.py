from django.urls import path
from .views import (
    ExamListAPIView,
    ExamDetailAPIView,
    SubmitExamAPIView,
    MySubmissionsAPIView,
)
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("exams/", ExamListAPIView.as_view()),
    path("exams/<int:exam_id>/", ExamDetailAPIView.as_view()),
    path("exams/<int:exam_id>/submit/", SubmitExamAPIView.as_view()),
    path("my-submissions/", MySubmissionsAPIView.as_view()),
    path('auth/token/', obtain_auth_token),
]
