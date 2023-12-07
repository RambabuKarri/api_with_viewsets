from django.shortcuts import render
from app.models import *
from app.serializers import *
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
# Create your views here.

class Boomer(ViewSet):
    def list(self,request):
        PO=Product.objects.all()
        JPO=ProductMSR(PO,many=True)
        return Response(JPO.data)
    def retrieve(self,request,pk):
        PO=Product.objects.get(pid=pk)
        JPO=ProductMSR(PO)
        return Response(JPO.data)
    def create(self,request):
        JD=ProductMSR(data=request.data)
        if JD.is_valid():
            JD.save()
            return Response({'message':'insertion is done'})
        return Response({'message':'invalid data'})
    def update(self,request,pk):
        PO=Product.objects.get(pid=pk)
        CPO=ProductMSR(PO,data=request.data)
        if CPO.is_valid():
            CPO.save()
            return Response({'message':'updation is done'})
        return Response({'message':'invalid data'})
    def partial_update(self,request,pk):
        PO=Product.objects.get(pid=pk)
        CPO=ProductMSR(PO,data=request.data,partial=True)
        if CPO.is_valid():
            CPO.save()
            return Response({'message':'updation is done'})
        return Response({'message':'invalid data'})
    def destroy(self,request,pk):
        PO=Product.objects.get(pid=pk)
        PO.delete()
        return Response({'message':'deletion is done'})
    
    

