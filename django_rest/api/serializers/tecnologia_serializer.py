from rest_framework import serializers
from ..models import Tecnologia


class TecnologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnologia
        fields = ('id', 'nome',) #mostra o id e nome no response