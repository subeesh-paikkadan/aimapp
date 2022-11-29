from django.contrib import admin

# Register your models here.
from .models import Gallery

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name','image')

admin.site.register(Gallery,GalleryAdmin)