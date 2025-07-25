from django.shortcuts import render
from cars.models import Car


def car_view(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')
    
    if search:
        cars = cars.filter(model__contains=search).order_by('model')
    
    return render(
        request,
        'cars.html',
        {'cars': cars}
    )

