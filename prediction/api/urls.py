from django.urls import path
from .views import get_prediction, health

urlpatterns = [
    path('prediction', get_prediction, name="get-prediction"),
    path('health', health)
]
