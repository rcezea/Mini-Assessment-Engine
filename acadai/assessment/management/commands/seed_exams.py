from django.core.management.base import BaseCommand
from assessment.models import Exam, Question


class Command(BaseCommand):
    help = "Seed database with exams and MCQ questions"

    def handle(self, *args, **kwargs):
        exams_data = [
            {
                "title": "Python Fundamentals",
                "course": "CS101",
                "questions": [
                    ("What is Python?", "A programming language", "A snake", "A database", "An OS", "A"),
                    ("Which keyword defines a function?", "func", "def", "lambda", "define", "B"),
                    ("Which type is immutable?", "list", "dict", "set", "tuple", "D"),
                    ("What does len() return?", "Memory size", "Length", "Index", "Type", "B"),
                    ("Which symbol starts a comment?", "//", "#", "/*", "--", "B"),
                    ("Which loop is conditional?", "for", "while", "foreach", "do", "B"),
                    ("What is PEP 8?", "Compiler", "Style guide", "Library", "IDE", "B"),
                    ("Which keyword handles exceptions?", "try", "catch", "handle", "error", "A"),
                    ("What is None?", "0", "False", "Null object", "Empty string", "C"),
                    ("Which structure uses key-value pairs?", "list", "tuple", "dict", "set", "C"),
                ],
            },
            {
                "title": "Data Structures",
                "course": "CS201",
                "questions": [
                    ("Stack follows?", "FIFO", "LIFO", "LILO", "FILO", "B"),
                    ("Queue follows?", "LIFO", "FIFO", "FILO", "LILO", "B"),
                    ("Which is non-linear?", "Array", "Linked list", "Tree", "Stack", "C"),
                    ("Binary search works on?", "Any list", "Sorted list", "Graph", "Tree", "B"),
                    ("Which DS uses nodes?", "Array", "List", "Linked list", "Set", "C"),
                    ("Hash table lookup is?", "O(n)", "O(log n)", "O(1)", "O(n²)", "C"),
                    ("Which uses recursion?", "Queue", "Tree traversal", "Stack", "Array", "B"),
                    ("Which stores hierarchy?", "Graph", "Tree", "List", "Set", "B"),
                    ("Which is LIFO?", "Queue", "Deque", "Stack", "Tree", "C"),
                    ("Which DS uses edges?", "Tree", "Graph", "Array", "Queue", "B"),
                ],
            },
            {
                "title": "Databases Basics",
                "course": "CS301",
                "questions": [
                    ("SQL stands for?", "Structured Query Language", "Simple Query Language", "Sequential Query", "Server Query", "A"),
                    ("Primary key is?", "Duplicate", "Unique", "Nullable", "Optional", "B"),
                    ("Which is NoSQL?", "Postgres", "MySQL", "MongoDB", "SQLite", "C"),
                    ("Which joins all rows?", "INNER", "LEFT", "RIGHT", "FULL", "D"),
                    ("Index improves?", "Storage", "Speed", "Security", "Memory", "B"),
                    ("Which clause filters rows?", "ORDER BY", "GROUP BY", "WHERE", "SELECT", "C"),
                    ("Which normal form removes duplication?", "1NF", "2NF", "3NF", "BCNF", "C"),
                    ("ACID stands for?", "Atomicity etc.", "Access etc.", "Async etc.", "None", "A"),
                    ("Which stores rows?", "Table", "Index", "View", "Trigger", "A"),
                    ("Which constraint enforces relation?", "UNIQUE", "CHECK", "FOREIGN KEY", "DEFAULT", "C"),
                ],
            },
        ]

        for exam_data in exams_data:
            exam, _ = Exam.objects.get_or_create(
                title=exam_data["title"],
                course=exam_data["course"],
                defaults={"duration_minutes": 30, "status": "PUBLISHED"},
            )

            for q in exam_data["questions"]:
                Question.objects.get_or_create(
                    exam=exam,
                    prompt=q[0],
                    defaults={
                        "question_type": "MCQ",
                        "option_a": q[1],
                        "option_b": q[2],
                        "option_c": q[3],
                        "option_d": q[4],
                        "expected_answer": q[5],
                    },
                )

        self.stdout.write(self.style.SUCCESS("✅ Exams and questions seeded successfully"))

        from assessment.management.commands.questions import (
            PYTHON_TEXT_QUESTIONS,
            DB_TEXT_QUESTIONS,
            DS_TEXT_QUESTIONS
        )

        TEXT_QUESTION_MAP = {
            "Python Fundamentals": PYTHON_TEXT_QUESTIONS,
            "Data Structures": DS_TEXT_QUESTIONS,
            "Databases Basics": DB_TEXT_QUESTIONS,
        }

        for exam in Exam.objects.filter(title__in=TEXT_QUESTION_MAP.keys()):
            for prompt, expected in TEXT_QUESTION_MAP[exam.title]:
                Question.objects.get_or_create(
                    exam=exam,
                    prompt=prompt,
                    defaults={
                        "question_type": "TEXT",
                        "expected_answer": expected,
                        "max_score": 5,
                    },
                )
