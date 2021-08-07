from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ListSerializer 

from .models import List_orderan

@api_view(['GET'])
def orderanOverview(request):
    api_urls = {
        'List':'/orderan-list/',
        'Detail View':'/orderan-detail/<str:pk>/',
        'Create':'/orderan-create/',
        'Update':'/orderan-update/<str:pk>/',
        'Delete':'/orderan-delete/<str:pk>/',
        }
    return Response(api_urls)

@api_view(['GET'])
def orderanlist(request):
    orderan = List_orderan.objects.all()
    serializer = ListSerializer(orderan, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def orderanDetail(request, pk):
    orderan = List_orderan.objects.get(id=pk)
    serializer = ListSerializer(orderan, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def orderanCreate(request):
    serializer = ListSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def orderanUpdate(request, pk):
    orderan = List_orderan.objects.get(id=pk)
    serializer = ListSerializer(instance=orderan, data=request.data)

    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['DELETE'])
def orderanDelete(request, pk):
    orderan = List_orderan.objects.get(id=pk)
    orderan.delete()

    return Response('Item Berhasil di Hapus')