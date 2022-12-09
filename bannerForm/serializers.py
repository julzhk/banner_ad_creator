from rest_framework import serializers

from . import models


class bannerAdSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.bannerAd
        fields = [
            "websiteURL",
            "created",
            "last_updated",
            "size",
            "emotion",
        ]

class EmotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Emotion
        fields = [
            "Name",
            "last_updated",
            "created",
            "slug",
        ]
