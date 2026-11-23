from django.shortcuts import render
from django.db.models import Prefetch
from .models import *


def data_veiw(request):
    
    return render(request, 'home.html')



def job_view(request):
    jobs = JobModel.objects.select_related('recruiter__company__user', 'category') 
    
    context = {
        'jobs': jobs
    }
    return render(request, 'job.html', context)



def job_detail_view(request):
    jobs = JobModel.objects.prefetch_related(
        Prefetch(
            'applications',
            queryset=ApplicationModel.objects.select_related('applicant')
        )
    )
    
    context = {
        'jobs': jobs
    }
    return render(request, 'companydata.html', context)



