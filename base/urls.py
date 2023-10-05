from django.urls import path
from .views import *


app_name = "base"


urlpatterns = [
    path('<str:website>/', EmailReceiver.as_view(), name='post-email'),
]
