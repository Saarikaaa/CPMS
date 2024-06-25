from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    d_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.d_name

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    batch = models.CharField(max_length=50, blank=True)
    cgpa = models.DecimalField(max_digits=3, decimal_places=2)
    cv = models.FileField(upload_to='cv_files/a.txt', null=True)
    date_of_birth = models.DateField(null=True)
    photo = models.ImageField(upload_to='student_photos/photo.jpg', null=True)

    def __str__(self):
        return self.name

class Company(models.Model):
    company_id = models.CharField(max_length=20, unique=True, null=True)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    establishment_year = models.CharField(max_length=4)
    industry_type = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name
    
class JobPosting(models.Model):
    job_id = models.AutoField(primary_key=True)
    company_id = models.CharField(max_length=20, null=True)
    job_title = models.CharField(max_length=100)
    job_requirement = models.CharField(max_length=1000)
    job_type = models.CharField(max_length=100)
    job_package = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='open')
    last_date = models.DateTimeField()

    def __str__(self):
        return self.job_title

class AppliedCandidates(models.Model):
    student_id = models.CharField(max_length=20, null=True)
    job_id = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)

class Notification(models.Model):
    student_id = models.CharField(max_length=20, null=True)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    