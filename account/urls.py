
from django.urls import path
from .views import *
app_name = "account"
urlpatterns = [
    path('signup/',user_create_view,name='signup_view'),
    path('logout/',logout_view,name="logout_view"),
    path('profile/', profile_detail_view, name= 'detail_view'),
    path('profile/create',profile_create_view,name='create_view'),
    path('login/',login_view,name="login_view")
    
]