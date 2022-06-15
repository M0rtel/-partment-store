from django.shortcuts import render
from .models import ApartmentCharacteristics, ApartmentCharacteristicsKV1, ApartmentCharacteristicsKV2, ApartmentCharacteristicsKV3, ApartmentCharacteristicsR

def recommendation(request):
    charR = ApartmentCharacteristicsR.objects.all()
    return render(request, 'products/recommendation.html', {'charR': charR})

def atelier(request):
    char = ApartmentCharacteristics.objects.all()
    return render(request, 'products/atelier.html', {'char': char})

def flat_1(request):
    char1 = ApartmentCharacteristicsKV1.objects.all()
    return render(request, 'products/flat_1.html', {'char1': char1})

def flat_2(request):
    char2 = ApartmentCharacteristicsKV2.objects.all()
    return render(request, 'products/flat_2.html', {'char2': char2})

def flat_3(request):
    char3 = ApartmentCharacteristicsKV3.objects.all()
    return render(request, 'products/flat_3.html', {'char3': char3})



