from rest_framework import serializers
from my_app.models import PortraitPhoto, FamilyPhoto, PregnantPhoto, WeddingPhoto
from my_app.models import Contact


class PortraitPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortraitPhoto
        fields = '__all__'

class FamilyPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyPhoto
        fields = '__all__'

class PregnantPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PregnantPhoto
        fields = '__all__'

class WeddingPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeddingPhoto
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'