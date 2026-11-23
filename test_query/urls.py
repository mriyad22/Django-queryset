from django.urls import path
from .views import *

app_name = 'test_query'

urlpatterns = [
    path('', data_veiw, name='data'),
    path('job/', job_view, name='job'),
]
