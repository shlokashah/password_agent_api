from django.urls import path,include
from users.views import registration_view
from rest_framework.authtoken.views import obtain_auth_token
from .views import create_website,list_websites
app_name = "users"

urlpatterns=[
	path('sites/',create_website,name='website'),
	path('sites/list/',list_websites,name='list'),
]

