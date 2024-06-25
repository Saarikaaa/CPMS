from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('student_login/', views.student_login, name='student_login'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('company_login/', views.company_login, name='company_login'),
    path('forgot_password/',auth_views.PasswordResetView.as_view(),name='forgot_password'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]