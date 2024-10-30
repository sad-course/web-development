from django.shortcuts import render

# Create your views here.
def IndexView(request):
    return render(request,"core/index.html")


def ImcCalculatorView(request):
    return render(request, "core/imc_calculator.html")