"""
URL configuration for cpms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_login/student_reg/register_student/', user_views.StudentUploadForm.as_view()),
    path('student_login/student_reg/', user_views.student_reg, name='student_reg'),
    path('student_login/student_reg/studreg_details', user_views.studreg_details, name='studreg_details'),
    path('dashboard/', user_views.stud_dashboard, name='stud_dashboard'),
    path('dashboard/upload_cv/', user_views.UploadCV.as_view()),
    path('dashboard/stud_apply_job', user_views.stud_apply_job, name='stud_apply_job'),
    path('dashboard/apply_job/', user_views.ApplyJobView.as_view()),
    path('dashboard/stud_results', user_views.stud_results, name='stud_results'),
    path('dashboard/logout', user_views.logout, name='logout'),

    path('company_login/comp_reg/register_company/', user_views.CompanyUploadForm.as_view()),
    path('company_login/comp_reg/', user_views.comp_reg, name='comp_reg'),
    path('company_login/comp_reg/compreg_details', user_views.compreg_details, name='compreg_details'),
    path('cdashboard/', user_views.comp_dashboard, name='comp_dashboard'),
    path('cdashboard/apply_post', user_views.apply_post, name='apply_post'),
    path('cdashboard/add_post/', user_views.ApplyPost.as_view()),
    path('cdashboard/posted_jobs', user_views.posted_jobs, name='posted_jobs'),
    path('cdashboard/stud_applications', user_views.stud_applications, name='stud_applications'),
    path('cdashboard/accept_application/', user_views.AcceptApplicationView.as_view()),
    path('cdashboard/stud_applications/reject_application', user_views.reject_application, name='reject_application'),
    path('delete_job/<int:job_id>/', user_views.delete_job_posting, name='delete_job_posting'),



    path('cdashboard/logout', user_views.logout, name='logout'),
    path('admin_tools_stats/', include('admin_tools_stats.urls')),
    path('', include('cpmsapp.urls')),

 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
