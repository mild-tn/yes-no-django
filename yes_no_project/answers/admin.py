from django.contrib.admin import ModelAdmin, register

from .models import Answer


@register(Answer)
class AnswerAdmin(ModelAdmin):
    list_display = ('id', 'text', 'image')
