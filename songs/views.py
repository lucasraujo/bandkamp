from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer


class SongView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_url_kwarg = "pk"

    def get_queryset(self):
        return Song.objects.filter(album_id=self.kwargs.get("pk"))
    
    def perform_create(self, serializer):
        return serializer.save(album_id=self.kwargs.get("pk"))
