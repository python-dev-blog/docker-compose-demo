from django.http import JsonResponse

from .models import Prediction


def get_prediction(request):
    return JsonResponse({"prediction": Prediction.objects.order_by('?').first().text})


def health(request):
    return JsonResponse({"status": "ok"})
