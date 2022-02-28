from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


class Picture(models.Model):
    img = models.ImageField(unique=True)
    name = models.CharField(max_length=50)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)


class Resizer(models.Model):
    img = models.ImageField(unique=True)
    small = ImageSpecField(source='img',
                           processors=[ResizeToFill(width=528, height=528)],
                           format='JPEG',
                           options={'quality': 1000})


class Avatar(models.Model):
    avatar = ProcessedImageField(upload_to='avatars', processors=[ResizeToFill(256, 100)], format='JPEG',
                                 options={'quality': 1920}, spec_id='avatar')
