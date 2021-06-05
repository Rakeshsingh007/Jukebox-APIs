from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from . models import Musicians
from albums.models import MusicAlbums
from . serializers import MusiciansSerializer
from albums.serializers import AlbumSerializer
from rest_framework import status
from rest_framework.pagination import PageNumberPagination




class MusiciansView(viewsets.ModelViewSet):

    """
    ViewSet for viewing and editing the Musicians .
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    serializer_class = MusiciansSerializer
    queryset = Musicians.objects.all()
    

    def create(self, request):
        """API to create musician"""

        serializer = MusiciansSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        data = serializer.data
        return Response({"status": "success", "data": data}, status=status.HTTP_201_CREATED)


    def partial_update(self, request, pk=None):

        """API to update musician"""

        queryset = Musicians.objects.filter(id=pk).first()
        serializer = MusiciansSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        data = serializer.data
        return Response({"status": "success", "data": data}, status=status.HTTP_200_OK)


    def list(self, request):

        """API to list musicians"""

        queryset = Musicians.objects.all().order_by('id')
        page = self.paginate_queryset(queryset)
        serializer = MusiciansSerializer(queryset, many=True)
        if page is not None:
            serializer = MusiciansSerializer(page, many=True)
        else:
            serializer = MusiciansSerializer(queryset, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):

        """API to get detail of  musician"""

        data = dict()
        queryset = Musicians.objects.filter(id=pk).first()
        if queryset:
        	data = MusiciansSerializer(queryset, many=False).data
        return Response({"status": "success", "data": data}, status=status.HTTP_200_OK)



class ListAlbumMusicians(APIView):

    """
    API to retrieve the list of musicians for a specified music album sorted by musician's Name in ascending order.

    """

    serializer_class = MusiciansSerializer

    def get(self, request, id):

        queryset = MusicAlbums.objects.prefetch_related('album_musicians').filter(id=id).first().album_musicians.all().order_by("musicians_name")
        data = MusiciansSerializer(queryset, many=True).data
        return Response({"status": "success", "data": data}, status=status.HTTP_200_OK)


class ListSortedAlbums(APIView):

    """
    API to retrieve the list of Music albums for a specified musician sorted by Price in ascending order (i.e Lowest first)

    """

    serializer_class = AlbumSerializer

    def get(self, request, id):

        queryset = Musicians.objects.filter(id=id).first().musicalbums_set.all().order_by("album_price")
        data = AlbumSerializer(queryset, many=True).data
        return Response({"status": "success", "data": data}, status=status.HTTP_200_OK)
