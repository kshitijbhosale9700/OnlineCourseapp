
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseNotAllowed

from .models import Course, Question, Choice, Submission


def submit(request, course_id):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    course = get_object_or_404(Course, id=course_id)

    # Get all questions belonging to this course's lessons
    questions = Question.objects.filter(lesson__course=course)

    # Get selected choices from the submitted form
    selected_ids = (
        request.POST.getlist("choices")
        or request.POST.getlist("choice")
    )

    selected_choices = Choice.objects.filter(
        id__in=selected_ids,
        question__in=questions
    )

    # Save the student's submission
    submission = Submission.objects.create(user=request.user)
    submission.questions.set(questions)
    submission.choices.set(selected_choices)

    # Display the exam result
    return show_exam_result(request, submission.id)


def show_exam_result(request, submission_id):
    submission = get_object_or_404(
        Submission,
        id=submission_id
    )

    total_questions = submission.questions.count()
    score = submission.choices.filter(is_correct=True).count()

    percentage = (
        (score / total_questions) * 100
        if total_questions > 0
        else 0
    )

    context = {
        "submission": submission,
        "total_questions": total_questions,
        "score": score,
        "percentage": percentage,
    }

    return render(request, "course/exam_result.html", context)