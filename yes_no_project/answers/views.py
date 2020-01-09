from django.shortcuts import render, redirect
from django.http import HttpResponse
from answers.models import Answer
from django.views import View
import random

# Create your views here.


def answer_view(requests):
    answers = Answer.objects.all()

    answerRnd = random.choice(answers)

    return render(
        requests,
        'answer.html',
        context={'answer': answerRnd}
    )


def create_answer_view(requests):
    return render(requests, 'create_answer.html')


def add_answer(request):
    text_field = request.POST['text']
    image_field = request.POST['image']
    if text_field or text_field:
        Answer.objects.create(
            text=text_field,
            image=image_field
        )
    return redirect('answer_views')


class CreateAnswerView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'create_answer.html')

    def post(self, request, *args, **kwargs):
        text_field = request.POST['text']
        image_field = request.POST['image']
        if text_field or text_field:
            Answer.objects.create(
                text=text_field,
                image=image_field
            )
        return render(request, 'answer.html')
