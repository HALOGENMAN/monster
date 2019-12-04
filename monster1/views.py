from django.shortcuts import render
from .models import Data
from .serializers import DataSerializers
from rest_framework.response import Response
from rest_framework.views import APIView 

# Create your views here.

class monster1View(APIView):

    def get(self,request,*args,**kwargs):
        qs = Data.objects.all()
        serializer = DataSerializers(qs,many=True)
        return Response(serializer.data)
