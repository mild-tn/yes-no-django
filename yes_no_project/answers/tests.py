from django.test import TestCase
# from django.urls import reverse
from answers.models import Answer


class CreateAnswerViewTest(TestCase):
    def test_create_answer_shold_save_model(self):
        response = self.client.post('/create_answer_class/', data={
            'text': 'yes',
            'image': 'https://media.giphy.com/media/ftqLysT45BJMagKFuk/giphy.gif'
        })
        self.assertEqual(response.status_code, 200)

        ans = Answer.objects.last()
        self.assertEqual(ans.text, 'yes')
        self.assertEqual(
            ans.image, 'https://media.giphy.com/media/ftqLysT45BJMagKFuk/giphy.gif')
