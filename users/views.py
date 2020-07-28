from django.contrib.auth import login,logout
from rest_framework import status 
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from users.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
import json
from django.core import serializers
# Create your views here.

'''/app/users/'''
# Registering New User
@api_view(['POST',])
def registration_view(request):
	print("viewww")
	if (request.method == 'POST'):
		print("idhar ayaa")
		serializer = RegistrationSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
			account = serializer.save()
			print('working')
			data['status'] = "account created"
			data['username'] = account.username
			token = Token.objects.get(user=account).key
			data['token'] = token
			return Response({'status':data['status']},content_type='application/json',status=201)
		else:
			data = serializer.errors
			print(data)
			return Response({'error':data},content_type='application/json',status=400)
	else:
		return Response({'failure':'error in data'},content_type='application/json',status=400)

'''/app/users/auth'''
# Logging the user in
class Login_view(ObtainAuthToken):
	def post(self, request, *args, **kwargs):
		serializer = self.serializer_class(data=request.data,context={'request': request})
		if (serializer.is_valid()):
			user = serializer.validated_data['user']
			token, created = Token.objects.get_or_create(user=user)
			print("Token",request.META.get("HTTP_AUTHORIZATION",""))
			return Response({'status':'success','user_id': user.pk,},content_type='application/json',status=200)
		else:
			return Response({'failure':'Credentials not valid'},content_type='application/json',status=400)
		
