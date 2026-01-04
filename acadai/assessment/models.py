from django.db import models


class Exam(models.Model):
    PUBLISHED = "PUBLISHED"
    CLOSED = "CLOSED"

    STATUS = [(PUBLISHED, "Published"), (CLOSED, "Closed")]

    title = models.CharField(max_length=255)
    course = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    metadata = models.JSONField(blank=True, null=True)
    status = models.TextField(max_length=10, choices=STATUS, default="DRAFT")

    def __str__(self):
        return self.title


class Question(models.Model):
    TEXT = "TEXT"
    MCQ = "MCQ"

    QUESTION_TYPES = [(TEXT, "Text"), (MCQ, "MCQ")]

    exam = models.ForeignKey(Exam, related_name="questions",
                             on_delete=models.CASCADE)
    question_type = models.CharField(max_length=10, choices=QUESTION_TYPES)
    prompt = models.TextField()
    option_a = models.CharField(max_length=255, blank=True)
    option_b = models.CharField(max_length=255, blank=True)
    option_c = models.CharField(max_length=255, blank=True)
    option_d = models.CharField(max_length=255, blank=True)
    expected_answer = models.TextField()
    max_score = models.FloatField(default=1)

    def __str__(self):
        return self.prompt[:50]
