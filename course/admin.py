from django.contrib import admin

from .models import (
    Course,
    Lesson,
    Instructor,
    Learner,
    Question,
    Choice,
    Submission,
)


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2


class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "order")
    inlines = [QuestionInline]


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("content", "lesson", "grade")
    inlines = [ChoiceInline]


class InstructorAdmin(admin.ModelAdmin):
    list_display = ("full_name", "user")


class LearnerAdmin(admin.ModelAdmin):
    list_display = ("user",)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("content", "question", "is_correct")


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "submitted_at")


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Learner, LearnerAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Submission, SubmissionAdmin)