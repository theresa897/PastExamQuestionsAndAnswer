from django.contrib import admin
from .models import School, Exam, Answer, User

admin.site.register(School)
admin.site.register(Exam)
admin.site.register(Answer)
admin.site.register(User)