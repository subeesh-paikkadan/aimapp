from django.contrib import admin

# Register your models here.
from quiz.models import Exam

class ExamAdmin(admin.ModelAdmin):
    pass
admin.site.register(Exam, ExamAdmin)