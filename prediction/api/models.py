from django.db import models


class Prediction(models.Model):
    text = models.TextField()
