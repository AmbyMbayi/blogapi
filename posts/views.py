from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerializer
from .models import Post

# Create your views here.


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
