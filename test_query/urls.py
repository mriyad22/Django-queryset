from django.urls import path
from .views import *
from .auths import *

app_name = 'test_query'

urlpatterns = [
    path('', data_veiw, name='data'),
    path('job/', job_view, name='job'),
    path('job/application/<int:job_id>/', job_applicant_view, name='jobs'),
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    
]
