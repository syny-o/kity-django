from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse


from .models import PortraitPhoto, PregnantPhoto, FamilyPhoto, WeddingPhoto
from .forms import ContactForm
from .api.serializers import PortraitPhotoSerializer, ContactSerializer, FamilyPhotoSerializer, PregnantPhotoSerializer, WeddingPhotoSerializer





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
                recipient_list=['synek.o@seznam.cz'],
            )

            messages.success(request, 'Email byl odeslán. Ozvu se Vám co nejdříve.')

            context = {    
                'form': form
            }

            base_url = reverse('home')
            contact_section = f"{base_url}#contact"
            
            return redirect(contact_section)



    if request.method == 'GET':

        form = ContactForm()
        
        # get photos data
        portrait_photos = PortraitPhoto.objects.all()
        pregnant_photos = PregnantPhoto.objects.all()
        family_photos = FamilyPhoto.objects.all()
        wedding_photos = WeddingPhoto.objects.all()

        context = {
            'portrait_photos': portrait_photos,
            'pregnant_photos': pregnant_photos,
            'family_photos': family_photos,
            'wedding_photos': wedding_photos,

            'form': form

        }


    return render(request, 'home.html', context)




def send_portrait_photos_to_api(request):
    if request.method == 'GET':
        photos = PortraitPhoto.objects.all()
        serializer = PortraitPhotoSerializer(photos, many=True)
        return JsonResponse(serializer.data, safe=False)

def send_family_photos_to_api(request):
    if request.method == 'GET':
        photos = FamilyPhoto.objects.all()
        serializer = FamilyPhotoSerializer(photos, many=True)
        return JsonResponse(serializer.data, safe=False)

def send_pregnant_photos_to_api(request):
    if request.method == 'GET':
        photos = PregnantPhoto.objects.all()
        serializer = PregnantPhotoSerializer(photos, many=True)
        return JsonResponse(serializer.data, safe=False)

def send_wedding_photos_to_api(request):
    if request.method == 'GET':
        photos = WeddingPhoto.objects.all()
        serializer = WeddingPhotoSerializer(photos, many=True)
        return JsonResponse(serializer.data, safe=False)






# only for DEBUG MODE
# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt

def receive_contact_from_api(request):
    if request.method == 'POST':


        serializer = ContactSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            name = serializer.data['name']
            email = serializer.data['email']
            message = serializer.data['message']
            send_mail(
                subject='marketasynkova.cz - Nová zpráva',
                message = f'Máš novou zprávu od {name} ({email})\n\n{message}',
                from_email='synekjbc@gmail.com',
                recipient_list=['synek.o@seznam.cz', 'marketa.synkova@gmail.com'],
            )
            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=400)

