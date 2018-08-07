# snippets/serializers
from rest_framework import serializers
from . models import Lion

class LionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lion
        fields='__all__'