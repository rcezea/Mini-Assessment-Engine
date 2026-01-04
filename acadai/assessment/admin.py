from django.contrib import admin
from .models import Submission, Answer, Exam, Question

# Register your models here.
admin.site.register(Submission)
admin.site.register(Answer)
admin.site.register(Exam)
admin.site.register(Question)
