from rest_framework import serializers

from .models import Picture, Resizer, Avatar


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = "__all__"


class SmallSerializer(serializers.ModelSerializer):
    small = serializers.ImageField(read_only=True)

    class Meta:
        model = Resizer
        fields = [
            'id',
            'img',
            'small',
        ]


class AvatarSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(read_only=False)

    class Meta:
        model = Avatar
        fields = "__all__"
