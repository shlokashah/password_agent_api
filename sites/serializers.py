from rest_framework import serializers
from sites.models import Sites
from django.contrib.auth.hashers import make_password

class SiteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sites
		fields = ['website','username','password']
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
	        user = Sites(
	            website = validated_data["website"],
	            username = validated_data["username"]
	        )
	        user.set_password(validated_data["password"])
	        user.save()
	        return user
