from rest_framework.viewsets import ModelViewSet
from lada.models import Lada
from lada.api.serializers import LadaSerializer

class LadaApiViewSet(ModelViewSet):
    serializer_class = LadaSerializer
    queryset = Lada.objects.all()