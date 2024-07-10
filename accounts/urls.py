from django.urls import path, include
from accounts import views


urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('register/',views.SignUp.as_view(),name='signup'),
    ]
