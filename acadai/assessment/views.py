from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from .models import Exam, Submission, Answer


class ExamListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        exams = Exam.objects.filter(status="PUBLISHED")

        data = [
            {
                "id": exam.id,
                "title": exam.title,
                "course": exam.course,
                "duration_minutes": exam.duration_minutes,
            }
            for exam in exams
        ]

        return Response(data)


class ExamDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, exam_id):
        exam = get_object_or_404(Exam, id=exam_id)

        return Response({
            "exam_id": exam.id,
            "title": exam.title,
            "duration": exam.duration_minutes,
            "questions": [
                {"id": q.id, "prompt": q.prompt, "A": q.option_a, "B": q.option_b, "C": q.option_c, "D": q.option_d}
                for q in exam.questions.all()
            ]
        })
