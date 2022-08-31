from socapi.models import Posts
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Mete:
        model=Posts
        exclude=["date",]
