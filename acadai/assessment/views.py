from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from .models import Exam, Submission, Answer
from .tasks import grade_submission


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


class SubmitExamAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, exam_id):
        exam = get_object_or_404(Exam, id=exam_id)

        if Submission.objects.filter(student=request.user, exam=exam).exists():
            return Response({"error": "Already submitted"}, status=400)

        answers = request.data.get("answers")

        if not isinstance(answers, dict):
            return Response(
                {"error": "Answers must be an object keyed by question_id"},
                status=400
            )

        submission = Submission.objects.create(student=request.user, exam=exam)

        for q_id, answer_text in answers.items():
            Answer.objects.create(
                submission=submission,
                question_id=q_id,
                text=answer_text
            )

        score = grade_submission(submission.id)
        return Response({"message": "Submitted successfully",
                         "score": f"{score}%"})


class MySubmissionsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        submissions = (
            Submission.objects
            .filter(student=request.user)
            .select_related("exam")
            .prefetch_related("answers")
        )

        data = []
        for s in submissions:
            data.append({
                "exam": s.exam.title,
                "score": f"{s.score}%",
                "graded": s.graded,
                "submitted_at": s.submitted_at
            })

        return Response(data)
