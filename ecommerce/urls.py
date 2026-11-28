from django.urls import path
from .views import *

app_name = 'ecommerce'

urlpatterns = [
     path('ecommerce/', ecommerce, name='ecommerce'),
 ]
 