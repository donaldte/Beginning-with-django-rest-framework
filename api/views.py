from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Serializations
from base.models import Item


@api_view(['GET'])
def getdata(request):
    item = Item.objects.all()
    serializer = Serializations(item, many=True)
    return Response(serializer.data)
    

@api_view(['POST'])
def postdata(request):
    serializer = Serializations(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)