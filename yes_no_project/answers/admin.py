from django.contrib import admin
from answers.models import Answer

# Register your models here.
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id','text','image')
