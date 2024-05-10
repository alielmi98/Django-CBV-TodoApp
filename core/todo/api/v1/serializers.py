from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from todo.models import Task
from django.contrib.auth.models import User


class Todoserializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            "id",
            "user",
            "title",
            "complete",
            "absolute_url",
            "created_date",
            "updated_date",
        ]
        read_only_fields = ["user"]

    def get_absolute_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

    def create(self, validated_data):
        validated_data["user"] = self.context.get("request").user
        return super().create(validated_data)
