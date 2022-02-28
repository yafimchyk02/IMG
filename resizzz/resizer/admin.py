from django.contrib import admin
from .models import *


class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_create', 'time_update')

    class Meta:
        model = Picture


admin.site.register(Picture, PictureAdmin)
# Register your models here.
