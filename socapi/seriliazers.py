from socapi.models import Posts
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Posts
        exclude=("date",)
