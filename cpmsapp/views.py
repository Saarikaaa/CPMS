from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import ForgotPasswordForm



def login_page(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        if user_type == 'student':
            return redirect('student_login')
        elif user_type == 'admin':
            return redirect('admin_login')
        elif user_type == 'company':
            return redirect('company_login')
    return render(request, 'cpmsapp/login.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin:index')  
        else:
            return render(request, 'cpmsapp/adminlogin.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'cpmsapp/adminlogin.html')

def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Student registered successfully!')
            return redirect('stud_dashboard')  
        else:
            return render(request, 'cpmsapp/stulogin.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'cpmsapp/stulogin.html')

def company_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('comp_dashboard')  # Replace 'success_url' with your desired success URL
        else:
            return render(request, 'cpmsapp/complogin.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'cpmsapp/complogin.html')

def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            # Process form data here (e.g., send password reset email)
            email = form.cleaned_data['email']
            return render(request, 'cpmsapp/forgot_email.html')  # Redirect to a password reset done page
    else:
        form = ForgotPasswordForm()
    return render(request, 'cpmsapp/forgot_pass.html', {'form': form})