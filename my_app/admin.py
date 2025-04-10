from django.contrib import admin

from .models import Contact, PortraitPhoto, PregnantPhoto, FamilyPhoto, WeddingPhoto, CommercePhoto


admin.site.register(Contact)
admin.site.register(PortraitPhoto)
admin.site.register(PregnantPhoto)
admin.site.register(FamilyPhoto)
admin.site.register(WeddingPhoto)
admin.site.register(CommercePhoto)
