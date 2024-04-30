from rest_framework import viewsets
from .models import AIModel
from .serializers import AIModelSerializer

class AIModelListView(viewsets.ModelViewSet):
    queryset = AIModel.objects.all()
    serializer_class = AIModelSerializer
