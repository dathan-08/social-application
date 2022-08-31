from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from socapi.seriliazers import PostSerializer
from rest_framework.response import Response
from socapi.models import Posts
# Create your views here.

class PostView(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Posts.objects.all()
        serializer=PostSerializer(qs,many=True)
        return Response(data=serializer.data)


