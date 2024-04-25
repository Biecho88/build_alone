from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ExcavatorForm
from .models import Excavator


def excavator(request):
    """ A view to return excavator for rent page """

    excavator = Excavator.objects.all()


    context = {
        'excavator': excavator,
    }

    return render(request, 'excavator/excavator.html', context)

@login_required
def add_excavator(request):
    """ Add a excavator to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

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
