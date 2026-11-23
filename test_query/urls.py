from django.urls import path
from .views import *

app_name = 'test_query'

urlpatterns = [
    path('', data_veiw, name='data'),
    path('job/', job_view, name='job'),
    path('job/application/', job_detail_view, name='jobs')
]
