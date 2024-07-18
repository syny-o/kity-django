from django.db import models

from .constants import PHOTO_TYPES



class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


# Abstract class
class Photo(models.Model):
    description = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
    type = models.CharField(max_length=1, choices=PHOTO_TYPES, default='P')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description} - {self.order} ({self.type})"

    class Meta:
        abstract = True
        ordering = ['-type', 'order']
    



class PortraitPhoto(Photo):
    image = models.ImageField(upload_to='portrait_photos/')


class PregnantPhoto(Photo):
    image = models.ImageField(upload_to='pregnant_photos/')


class FamilyPhoto(Photo):
    image = models.ImageField(upload_to='family_photos/')


class WeddingPhoto(Photo):
    image = models.ImageField(upload_to='wedding_photos/')



