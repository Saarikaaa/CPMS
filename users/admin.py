
from django.contrib import admin
from .models import Department, Student, Company, AppliedCandidates, JobPosting
from import_export.admin import ExportMixin
from import_export import resources


class StudentResource(resources.ModelResource):
    class Meta:
        model = Student


class StudentAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = StudentResource
    list_display = ['student_id', 'name', 'date_of_birth', 'email', 'department', 'cgpa', 'cv', 'photo']
    search_fields = ['name', 'email']
    list_filter = ['department']


class AppliedCandidatesResource(resources.ModelResource):
    class Meta:
        model = AppliedCandidates


class AppliedCandidatesAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = AppliedCandidatesResource
    list_display = ['student_id', 'job_id', 'accepted']
    search_fields = ['student_id', 'job_id', 'accepted']
    list_filter = ['student_id', 'job_id', 'accepted']


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_id', 'company_name', 'location', 'establishment_year', 'industry_type']
    search_fields = ['company_id', 'company_name', 'location']
    list_filter = ['industry_type']


class JobPostingAdmin(admin.ModelAdmin):
    list_display = ['company_id', 'job_title', 'job_requirement', 'job_type', 'job_package', 'last_date']
    search_fields = ['company_id', 'job_title', 'job_type']
    list_filter = ['job_type', 'job_package']


admin.site.register(Department)
admin.site.register(JobPosting, JobPostingAdmin)
admin.site.register(AppliedCandidates, AppliedCandidatesAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Student, StudentAdmin)
