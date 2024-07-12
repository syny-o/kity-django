from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm




def home(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Email sent successfully.')
            return redirect('home')

    else:
        form = ContactForm()

    context = {
        'form': form
    }


    return render(request, 'home.html', context)
