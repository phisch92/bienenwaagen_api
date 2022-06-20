# core/views.py
from rest_framework import generics

from .models import Scale
from .serializers import ScaleSerializer

class ScaleList(generics.ListCreateAPIView):
    queryset = Scale.objects.all()
    serializer_class = ScaleSerializer
    
class ScaleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Scale.objects.all()
    serializer_class = ScaleSerializer