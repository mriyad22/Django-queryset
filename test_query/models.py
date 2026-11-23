from django.db import models
from django.contrib.auth.models import User


class CompanyModel(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="company_profile",
        null=True, 
        blank=True
    )
    
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class CategoryModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class RecruiterModel(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(
        CompanyModel,
        on_delete=models.CASCADE,
        related_name="recruiters"
    )

    def __str__(self):
        return self.name


class JobModel(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    salary = models.PositiveIntegerField()
    recruiter = models.ForeignKey(
        RecruiterModel,
        on_delete=models.CASCADE,
        related_name="jobs"
    )

    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.CASCADE,
        related_name="jobs"
    )

    def __str__(self):
        return self.title




class ApplicationModel(models.Model):
    job = models.ForeignKey(
        JobModel,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    applicant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="job_applications"
    )

    status = models.CharField(
        max_length=20,
        default="Pending"
    )

    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.username} - {self.job.title}"
