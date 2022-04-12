from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework import filters
from rest_framework import mixins

from .serializers import CommentSerializer, PostSerializer, GroupSerializer
from posts.models import Group, Post, Comment, User


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
