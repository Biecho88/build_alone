from django.shortcuts import render
from .models import Excavator

from .forms import ExcavatorForm


def excavator(request):
    """ A view to return excavator for rent page """

    excavator = Excavator.objects.all()


    context = {
        'excavator': excavator,
    }

    return render(request, 'excavator/excavator.html', context)


def add_excavator(request):
    """ Add a product to the store """
    form = ExcavatorForm()
    template = 'excavator/add_excavator.html'
    context = {
        'form': form,
    }

    return render(request, template, context)