import random
import datetime
from time import sleep
from celery import shared_task

from api.models import Prediction
from api.utils import build_generator, generate_text
from prediction.celery import app


@app.task
def generate_predictions():
    generator = build_generator()
    for _ in range(random.randint(1, 40)):
        Prediction(text=generate_text(generator, random.randint(1, 20))).save()
