from django.urls import path
from .views import IndexView, ImcCalculatorView

urlpatterns = [
    path("", IndexView, name="homepage"),
    path("imc-calculator/", ImcCalculatorView, name="imc-calculator")
]