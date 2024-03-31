#from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Drink, Snack
from .serializers import DrinkSerializer, SnackSerializer

class DrinkViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,*args,**kwargs):
        '''
        list all drinks
        '''
        #drinks = Drink.objects.filter(user = request.user.id)
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        '''
        create new drinks entry
        '''
        data = {
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'type': request.data.get('type')
        }
        serializer = DrinkSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnackViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''
        list all snacks
        '''

        snacks = Snack.objects.all()
        serializer = DrinkSerializer(snacks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        create new snacks entry
        '''
        data = {
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'type': request.data.get('type')
        }
        serializer = SnackSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def drink_list(request):
#     #get all drinks
#     drinks = Drink.objects.all()
#     #serialize data
#     serializer = DrinkSerializer(drinks, many=True)
#     return JsonResponse({'all_drinks':serializer.data}, safe=False)
#
# def snack_list(request):
#     #get all drinks
#     snacks = Snack.objects.all()
#     #serialize data
#     serializer = SnackSerializer(snacks, many=True)
#     return JsonResponse({'all_snacks': serializer.data}, safe=False)