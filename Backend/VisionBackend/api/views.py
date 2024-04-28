from rest_framework import generics
from .models import AIModel
from .serializers import AIModelSerializer

class AIModelListView(generics.ListAPIView):
    queryset = AIModel.objects.all()
    serializer_class = AIModelSerializer
