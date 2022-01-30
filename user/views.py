from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from .permissions import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny


# Create your views here.


class PostUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = PostSerializers
    queryset = Post.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializers
    permission_classes = (IsAuthenticated, )


class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializers
    queryset = Post.objects.all()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
