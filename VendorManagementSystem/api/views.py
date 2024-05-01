from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# vendor create/list
class VendorCreate(APIView):
    # vender List
    def get(self,request):
        vendor=Vendor.objects.all()
        serializer=VendorSerializer(vendor, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Vendor Create
    def post(self,request):
        serializer=VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# vendor details 
class VendorDetails(APIView):
    # Fetching vendor acc. to id
    def get(self,request, pk):
        try:
            vendor=Vendor.objects.get(pk=pk)
        except:
            return Response({'error':'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer=VendorSerializer(vendor)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Updating vendor info
    def put(self,request,pk):
        vendor=Vendor.objects.get(pk=pk)
        serializer=VendorSerializer(vendor,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        try:
            vendor=Vendor.objects.get(pk=pk)
        except:
            return Response({"msg":"Vendor not found"}, status=status.HTTP_404_NOT_FOUND)
        vendor.delete()
        return Response({'data':'task deleted'}, status=status.HTTP_204_NO_CONTENT)


# Purchase Order  
class PurchaseOrderCreate(APIView):
    def get(self,request):
        order=PurchaseOrder.objects.all()
        serializer=PurchaseOrderSerializer(order, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    
