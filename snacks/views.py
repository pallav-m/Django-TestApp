# from django.http import JsonResponse
from django.contrib.auth import authenticate
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Drink, Snack
from .serializers import DrinkSerializer, SnackSerializer, LoginSerializer, RegisterSerializer, DeleteUserSerializer


class DrinkViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, *args, **kwargs):
        '''
        list all drinks
        '''
        # drinks = Drink.objects.filter(user = request.user.id)
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
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


class DrinkDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self, drink_id):
        '''
        Helper method to get the object with given todo_id, and user_id
        '''
        try:
            return Drink.objects.get(id=drink_id)
        except Drink.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, drink_id, *args, **kwargs):
        '''
        Retrieves the drink with given id
        '''
        drink_instance = self.get_object(drink_id)
        if not drink_instance:
            return Response(
                {"res": "Drink with given id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = DrinkSerializer(drink_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, drink_id, *args, **kwargs):
        '''
        Updates the drink item with given drink_id if it exists
        '''
        drink_instance = self.get_object(drink_id)
        if not drink_instance:
            return Response(
                {"res": "Drink with given drink_id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'type': request.data.get('type')
        }
        serializer = DrinkSerializer(instance=drink_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, drink_id, *args, **kwargs):
        '''
        Deletes the drink item with given drink_id if it exists
        '''
        drink_instance = self.get_object(drink_id)
        if not drink_instance:
            return Response(
                {"res": "Drink with given id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        drink_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class SnackViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

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


class SnackDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self, snack_id):
        '''
        Helper method to get the object with given snack_id
        '''
        try:
            return Snack.objects.get(id=snack_id)
        except Snack.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, snack_id, *args, **kwargs):
        '''
        Retrieves the snack with given snack_id
        '''
        snack_instance = self.get_object(snack_id)
        if not snack_instance:
            return Response(
                {"res": "Snack with given id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = SnackSerializer(snack_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, snack_id, *args, **kwargs):
        '''
        Updates the snack item with given snack_id if it exists
        '''
        snack_instance = self.get_object(snack_id)
        if not snack_instance:
            return Response(
                {"res": "Snack with given snack_id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'type': request.data.get('type')
        }
        serializer = SnackSerializer(instance=snack_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, snack_id, *args, **kwargs):
        '''
        Deletes the snack item with given snack_id if it exists
        '''
        snack_instance = self.get_object(snack_id)
        if not snack_instance:
            return Response(
                {"res": "Snack with given snack_id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        snack_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class LoginAPI(APIView):

    def post(self, request):
        request_data = request.data
        serializer = LoginSerializer(data=request_data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=request_data['username'], password=request_data['password'])
        #print(user)

        if not user:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        token, created = Token.objects.get_or_create(user=user)
        return Response({'message': 'login successful', 'token': str(token)}, status=status.HTTP_200_OK)


class RegisterUser(APIView):

    def post(self, request):
        request_data = request.data
        serializer = RegisterSerializer(data=request_data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response({'message': f'user created'}, status=status.HTTP_201_CREATED)


class DeleteUserAPI(APIView):

    def delete(self, request):
        request_data = request.data
        serializer = DeleteUserSerializer(data=request_data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=request_data['username'], password=request_data['password'])
        if not user:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

