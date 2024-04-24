from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Excavator
from django.contrib import messages

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
    if request.method == 'POST':
        form = ExcavatorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added excavator!')
            return redirect(reverse('add_excavator'))
        else:
            messages.error(request, 'Failed to add excavator. Please ensure the form is valid.')
    else:
        form = ExcavatorForm()
    
    template = 'excavator/add_excavator.html'
    context = {
        'form': form,
    }

    return render(request, template, context)