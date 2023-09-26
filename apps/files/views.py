from rest_framework import viewsets

from .models import File
from .serializers import FileSerializer
from core.permissions import IsSubscriber


class FileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsSubscriber]