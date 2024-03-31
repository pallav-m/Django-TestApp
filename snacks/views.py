from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Drink, Snack
from .serializers import DrinkSerializer, SnackSerializer

# class DrinkViewSet(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get(self,request,*args,**kwargs):
#         '''
#         list all drinks
#         '''
#         #drinks = Drink.objects.filter(user = request.user.id)
#         drinks = Drink.objects.all()
#         serializer = DrinkSerializer(drinks, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
def drink_list(request):
    #get all drinks
    drinks = Drink.objects.all()
    #serialize data
    serializer = DrinkSerializer(drinks, many=True)
    return JsonResponse({'all_drinks':serializer.data}, safe=False)

def snack_list(request):
    #get all drinks
    snacks = Snack.objects.all()
    #serialize data
    serializer = SnackSerializer(snacks, many=True)
    return JsonResponse({'all_snacks': serializer.data}, safe=False)