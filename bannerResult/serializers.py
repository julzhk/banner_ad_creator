from rest_framework import serializers

from . import models


class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Result
        fields = [
            "last_updated",
            "created",
            "image",
        ]
