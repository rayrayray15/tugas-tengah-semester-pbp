from rest_framework import serializers
from beranda import models

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "name",
            "email",
            "comments"
        )
        model = models.Feedback