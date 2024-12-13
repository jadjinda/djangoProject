from rest_framework import serializers

from compte.models import Compte


class CompteSerializer(serializers.Serializer):
    class Meta:
        model = Compte
        fields = '__all__'