from django.shortcuts import render
from .models import Excavator

# Create your views here.

def excavator(request):
    """ A view to return excavator for rent page """

    excavator = Excavator.objects.all()


    context = {
        'excavator': excavator,
    }

    return render(request, 'excavator/excavator.html', context)