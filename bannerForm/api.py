from rest_framework import viewsets, permissions

from . import serializers
from . import models


class bannerAdViewSet(viewsets.ModelViewSet):
    """ViewSet for the bannerAd class"""

    queryset = models.bannerAd.objects.all()
    serializer_class = serializers.bannerAdSerializer
    permission_classes = [permissions.IsAuthenticated]


class EmotionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Emotion class"""

    queryset = models.Emotion.objects.all()
    serializer_class = serializers.EmotionSerializer
    permission_classes = [permissions.IsAuthenticated]
