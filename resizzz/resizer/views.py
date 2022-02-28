from rest_framework import generics

from .models import Picture, Resizer, Avatar
from .serializers import PictureSerializer, SmallSerializer, AvatarSerializer


class PictureAPIList(generics.ListCreateAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class PictureAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class SmallAPIList(generics.ListCreateAPIView):
    queryset = Resizer.objects.all()
    serializer_class = SmallSerializer


class AvatarAPIList(generics.ListCreateAPIView):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer

# Create your views here.
