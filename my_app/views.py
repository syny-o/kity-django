from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail


from .models import PortraitPhoto
from .forms import ContactForm





def home(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()


            # get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            
            # send mail
            send_mail(
                subject='Contact Form',
                message = f'You have a new message from {name} ({email})\n\n{message}',
                from_email='django@demomailtrap.com',
                recipient_list=['synek.o@seznam.cz', 'synekjbc@gmail.com'],
            )

            messages.success(request, 'Email sent successfully.')

            context = {    
                'form': form
            }

            return redirect('home')



    if request.method == 'GET':

        form = ContactForm()
        
        # get photos data
        portrait_photos = PortraitPhoto.objects.all()

        context = {
            'portrait_photos': portrait_photos,
            'form': form

        }


    return render(request, 'home.html', context)
