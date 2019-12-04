from rest_framework import serializers
from .models import POst

class POstSerializers(serializers.ModelSerializer):
    class Meta:
        model = POst
        fields = "__all__"