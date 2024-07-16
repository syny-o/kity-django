from django.db import models

from .constants import PHOTO_TYPES



class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    



class PortraitPhoto(models.Model):


    image = models.ImageField(upload_to='portrait_photos/')
    description = models.CharField(max_length=255)
    
    order = models.IntegerField(default=0)
    type = models.CharField(max_length=1, choices=PHOTO_TYPES, default='P')

    
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.description
    

    class Meta:
        ordering = ['-type', 'order']





class PregnantPhoto(models.Model):


    image = models.ImageField(upload_to='pregnant_photos/')
    description = models.CharField(max_length=255)
    
    order = models.IntegerField(default=0)
    type = models.CharField(max_length=1, choices=PHOTO_TYPES, default='P')

    
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.description
    

    class Meta:
        ordering = ['-type', 'order']    





class FamilyPhoto(models.Model):


    image = models.ImageField(upload_to='family_photos/')
    description = models.CharField(max_length=255)
    
    order = models.IntegerField(default=0)
    type = models.CharField(max_length=1, choices=PHOTO_TYPES, default='P')

    
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.description
    

    class Meta:
        ordering = ['-type', 'order']                



