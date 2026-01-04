from .models import Submission
from .services import grade_text_answer


def grade_submission(submission_id):
    submission = (Submission.objects.select_related("exam")
                  .prefetch_related("answers__question")
                  .get(id=submission_id))

    total = 0
    max_total = 0

    for idx, ans in enumerate(submission.answers.all()):
        q = ans.question

        if q.question_type == "MCQ":
            if ans.text.strip().upper() == q.expected_answer.strip().upper():
                # print("First", idx, "Text: ", ans.text, " Expected: ", q.expected_answer)
                question_score = q.max_score
            else:
                # print("Second", idx, "Text: ", ans.text, " Expected: ", q.expected_answer)
                question_score = 0

        elif q.question_type == "TEXT":
            similarity = grade_text_answer(ans.text, q.expected_answer)
            question_score = similarity * q.max_score

        ans.score = question_score
        ans.save()

        total += question_score
        max_total += q.max_score

    # print(total, max_total)

    score = round((total / max_total) * 100, 2) if max_total else 0
    submission.score = score
    submission.graded = True
    submission.save()
    return score
