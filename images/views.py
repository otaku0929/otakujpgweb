from django.shortcuts import render
from rest_framework import viewsets, status

from images.models import Image
from images.serializers import ImageSerializer
from ptt_beauty_images import settings

from rest_framework.response import Response
from rest_framework.decorators import list_route


# single-databases
def index(request):
    return render(request, 'index.html', {
        'images': Image.objects.values('id', 'Url').order_by('-CreateDate')
    })


# Create your views here.
class ImageViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    # [ GET ] /api/image/random/
    @list_route(methods=['get'], url_path='random')
    def get_random_image(self, request):
        image = Image.objects.all().order_by('?')[1]
        result = ImageSerializer(image)
        return Response(result.data, status=status.HTTP_200_OK)
