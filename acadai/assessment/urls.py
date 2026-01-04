from django.urls import path
from .views import (
    ExamListAPIView,
    ExamDetailAPIView,
    SubmitExamAPIView,
    MySubmissionsAPIView,
)
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path("exams/", ExamListAPIView.as_view()),
    path("exams/<int:exam_id>/", ExamDetailAPIView.as_view()),
    path("exams/<int:exam_id>/submit/", SubmitExamAPIView.as_view()),
    path("my-submissions/", MySubmissionsAPIView.as_view()),
    path('auth/token/', obtain_auth_token),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
