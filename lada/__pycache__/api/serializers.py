from rest_framework.serializers import ModelSerializer
from lada.models import Lada

class LadaSerializer(ModelSerializer):
    class Meta:
        model = Lada
        fields = ['id','Anno','Marca','Color','Combustible','NumPuertas','Traccion']