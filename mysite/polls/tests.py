from django.test import TestCase
from django.utils import timezone
import datetime
from .models import Question

# Create your tests here.


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)


    def test_was_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, second=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self_):
        time = timezone.now() - datetime.timedelta(hourso=23, minutes=59, secinds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)