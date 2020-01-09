from django.core.management.base import BaseCommand

import requests

from answers.models import Answer


class Command(BaseCommand):
    help = 'Get answer from http://yesno.wft/api API'

    def add_arguments(self, parser):
        parser.add_argument(
            'force_type',
            type=str,
            help='You can force by send "yes" or "no".'
        )

    def handle(self, *args, **options):
        param = options['force_type']
        url = f'http://yesno.wtf/api/?force={param}'
        response = requests.get(url)
        data = response.json()
        answer = Answer.objects.create(
            text=data['answer'],
            image=data['image']
        )

        message = f'created: {str(answer.id)} {answer.text} {answer.image}'

        self.stdout.write(message, ending='')
