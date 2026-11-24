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



def job_applicant_view(request, job_id):
    jobs = JobModel.objects.prefetch_related(
        Prefetch(
            'applications',
            queryset=ApplicationModel.objects.select_related('applicant'),
            to_attr='seeker'
        )
    ).get(id = job_id)
    
    # jobs = JobModel.objects.get(id = job_id)
    
    context = {
        'job': jobs
    }
    return render(request, 'companydata.html', context)



