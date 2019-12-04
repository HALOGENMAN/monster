from django.shortcuts import render
from .models import Data
from .serializers import DataSerializers
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework import generics,mixins
# Create your views here.

class monster1View(generics.GenericAPIView,mixins.CreateModelMixin,
                                           mixins.ListModelMixin,
                                           mixins.RetrieveModelMixin,
                                           mixins.DestroyModelMixin,
                                           mixins.UpdateModelMixin):

    serializer_class = DataSerializers
    queryset = Data.objects.all()
    lookup_field = "id"
    def get(self,request,id = None):
        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
    def put(self,request,id = None):
        return self.update(request,id)

    def delete(self,request,id = None):
        return self.delete(request,id)
       
