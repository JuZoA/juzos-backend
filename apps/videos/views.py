from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Video
from .serializers import VideoSerializer




class VideoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer