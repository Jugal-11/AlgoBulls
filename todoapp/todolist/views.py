from django.shortcuts import render

from rest_framework import generics
from .models import ToDoItem
from .serializers import ToDoItemSerializer

class ToDoItemListCreateView(generics.ListCreateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer


class ToDoItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
