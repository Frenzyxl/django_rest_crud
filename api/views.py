from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addData(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def updateData(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        return Response(status=404)

    serializer = ItemSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def deleteData(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        return Response(status=404)

    serializer = ItemSerializer(item)
    item.delete()
    return Response(serializer.data, status=204)

