from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


from .models import PortraitPhoto, PregnantPhoto, FamilyPhoto, WeddingPhoto, CommercePhoto

from .api.serializers import PortraitPhotoSerializer, ContactSerializer, FamilyPhotoSerializer, PregnantPhotoSerializer, WeddingPhotoSerializer, CommercePhotoSerializer












@require_http_methods(["GET"])
def send_portrait_photos_to_api(request):
    try:
        photos = PortraitPhoto.objects.all()
        serializer = PortraitPhotoSerializer(photos, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)  # Úspěšný požadavek
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)  # Interní chyba serveru


@require_http_methods(["GET"])
def send_family_photos_to_api(request):
    try:
        photos = FamilyPhoto.objects.all()
        serializer = FamilyPhotoSerializer(photos, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@require_http_methods(["GET"])
def send_pregnant_photos_to_api(request):
    try:
        photos = PregnantPhoto.objects.all()
        serializer = PregnantPhotoSerializer(photos, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@require_http_methods(["GET"])
def send_wedding_photos_to_api(request):
    try:
        photos = WeddingPhoto.objects.all()
        serializer = WeddingPhotoSerializer(photos, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@require_http_methods(["GET"])
def send_commerce_photos_to_api(request):
    try:
        photos = CommercePhoto.objects.all()
        serializer = CommercePhotoSerializer(photos, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)








import logging
log = logging.getLogger(__name__)

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

def receive_contact_from_api(request):
    if request.method == 'POST':


        serializer = ContactSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            name = serializer.data['name']
            email = serializer.data['email']
            message = serializer.data['message']
            try:
                log.info("contact email: sending")
                send_mail(
                    subject='marketasynkova.cz - Nová zpráva',
                    message = f'Máš novou zprávu od {name} ({email})\n\n{message}',
                    from_email='info@marketasynkova.cz',
                    recipient_list=['synek.o@seznam.cz', 'marketa.synkova@gmail.com'],
                )
                log.info("contact email: sent")
            except Exception as e:
                # neshodí request; jen zaloguješ důvod (SMTP/DNS/timeout…)
                log.exception("contact email failed: %s", e)
            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=400)

