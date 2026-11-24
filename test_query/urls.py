from django.urls import path
from .views import *

app_name = 'test_query'

urlpatterns = [
    path('', data_veiw, name='data'),
    path('job/', job_view, name='job'),
    path('job/application/<int:job_id>/', job_applicant_view, name='jobs')
]
