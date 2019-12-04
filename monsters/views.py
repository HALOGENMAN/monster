from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import POstSerializers
from .models import POst
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class TestView(APIView):
    
    permission_classes = (IsAuthenticated,)

    def get(self,request,*args,**kwargs):
        qs = POst.objects.all()
        serializer = POstSerializers(qs,many=True)
        return Response(serializer.data)
    
    def post(self,request,*args,**kwargs):
        serializer = POstSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)
        return Response(serializer.errors)

