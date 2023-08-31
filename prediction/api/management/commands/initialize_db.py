from django.core.management.base import BaseCommand

from api.models import Prediction


class Command(BaseCommand):
    help = 'Initialize db with prediction from predictions.txt'

    def handle(self, *args, **options):
        if not Prediction.objects.count():
            with open("predictions.txt", "r") as file:
                for prediction in file.readlines():
                    Prediction(text=prediction.replace('\n', '')).save()
        self.stdout.write(self.style.SUCCESS('Initialize db command executed successfully'))
