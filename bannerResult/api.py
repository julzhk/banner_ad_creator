from rest_framework import viewsets, permissions

from . import serializers
from . import models


class ResultViewSet(viewsets.ModelViewSet):
    """ViewSet for the Result class"""

    queryset = models.Result.objects.all()
    serializer_class = serializers.ResultSerializer
    permission_classes = [permissions.IsAuthenticated]
