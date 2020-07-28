from django.urls import path,include
from users.views import registration_view
from rest_framework.authtoken.views import obtain_auth_token
from .views import Login_view
app_name = "users"

urlpatterns=[
	path('users/',registration_view,name='register'),
	path('users/auth/',Login_view.as_view(),name="login"),
]

