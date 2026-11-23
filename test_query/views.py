from django.shortcuts import render
from .models import *


def data_veiw(request):
    
    return render(request, 'home.html')



def job_view(request):
    jobs = JobModel.objects.all()
    
    context = {
        'jobs': jobs
    }
    return render(request, 'job.html', context)



