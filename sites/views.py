from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from sites.models import Sites
from sites.serializers import SiteSerializer
import json
from .tokens import password_token
# Create your views here.

'''/app/sites/'''
@api_view(['POST',])
@permission_classes([IsAuthenticated,])
def create_website(request):
	user = request.query_params['user']
	user_instance = User.objects.get(pk = user)
	website = Sites(user=user_instance)
	if request.method =='POST':
		serializer = SiteSerializer(website,data=request.data)
		# data = {}
		if serializer.is_valid():
			# serializer.author = request.user
			# token = account_activation_token.make_token()
			serializer.save()
			# print(serializer['password'])
			return Response({'status':'success'},status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

'''app/sites/list/'''
@api_view(['GET',])
@permission_classes([IsAuthenticated,])
def list_websites(request):
	if request.method == 'GET':
		try:
			user = request.query_params['user']
			user_instance = User.objects.get(pk = user)
			print(user_instance)
			website = Sites.objects.filter(user = user_instance).values()
			print(website)
			qs = json.dumps(list(website.values()))
			print(qs)
			return Response(qs)
		except Sites.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
