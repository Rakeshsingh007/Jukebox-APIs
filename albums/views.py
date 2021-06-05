from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from . models import MusicAlbums
from . serializers import AlbumSerializer
from rest_framework import status
from rest_framework.pagination import PageNumberPagination




class MusicAlbumsView(viewsets.ModelViewSet):

    """
    A simple ViewSet for viewing and editing the MusicAlbums and 
    associated with the Musicians.
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    serializer_class = AlbumSerializer
    queryset = MusicAlbums.objects.all()
    

    def create(self, request):

        """API to create albums"""

        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        data = serializer.data
        return Response({"status": "success", "data": data}, status=status.HTTP_201_CREATED)


    def partial_update(self, request, pk=None):

        """API to update albums"""

        queryset = MusicAlbums.objects.filter(id=pk).first()
        serializer = AlbumSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        data = serializer.data
        return Response({"status": "success", "data": data}, status=status.HTTP_200_OK)


    def list(self, request):

        """
        API to retrieve the list of Music albums sorted by Date of release in ascending order (i.e Oldest first)
        """

        queryset = MusicAlbums.objects.all().order_by('album_release_date')
        page = self.paginate_queryset(queryset)
        serializer = AlbumSerializer(queryset, many=True)
        if page is not None:
            serializer = AlbumSerializer(page, many=True)
        else:
            serializer = AlbumSerializer(queryset, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):

        """API to get detail of  albums"""

        data = dict()
        queryset = MusicAlbums.objects.filter(id=pk).first()
        if queryset:
        	data = AlbumSerializer(queryset, many=False).data
        return Response({"status": "success", "data": data}, status=status.HTTP_200_OK)
