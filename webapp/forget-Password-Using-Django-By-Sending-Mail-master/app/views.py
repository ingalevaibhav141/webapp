from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
import uuid
from django.conf import settings
from .models import Profile
from django.core.mail import send_mail

from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.views import View
from .models import student
from .forms import AddstudentForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email=request.POST['email']
        user = User.objects.create_user(username=username,password=password,email=email)
        ftoken = str(uuid.uuid4())
        profile = Profile.objects.create(user=user,forget_token=ftoken)
        if profile and user:
            messages.success(request, 'Profile Created! please log in')
    return render(request,'login.html')

from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Redirect to a success page or any other desired page
            return redirect('home1')
        else:
            # Handle invalid login credentials
            return render(request, 'login1.html', {'error_message': 'Invalid username or password.'})
    
    return render(request, 'login1.html')



def fpass(request):
    if request.method == 'POST':
        username = request.POST['username']
        user = User.objects.get(username=username)
        print(user.check_password("admin"))
        profile = Profile.objects.get(user=user)
        user_email = user.email
        print(user_email)
        ftoken = profile.forget_token
        mail_message = f'Hey Your Reset Password Link is http://127.0.0.1:8081/changepass/{ftoken}/'
        send_mail('Password Reset Request',mail_message,settings.EMAIL_HOST_USER,[user_email],fail_silently=False)
        messages.success(request,'MAIL SEND')
    return render(request,'forgetpassword.html')

def changepassword(request,id):
    if request.method == 'POST':
        password = request.POST['password']
        profile = Profile.objects.get(forget_token=id).user
        user = User.objects.get(username=profile)
        user.set_password(password)
        user.save()
        messages.success(request,'Password Changed Please Login! ')
        return redirect('main')
    return render(request,'changepassword.html')

def main(request):
    return render(request,'index.html')

def LogoutPage(request):
     logout(request)
        
     return redirect('login')


# crud

class Home1(View):
    def get(self, request):
        stu_data = student.objects.all()
        return render(request, 'home1.html', {'studata': stu_data})

class Add_student(View):
    def get(self, request):
        fm = AddstudentForm()
        return render(request, 'add-student.html', {'form': fm})

    def post(self, request):
        fm = AddstudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('home1')
        else:
            return render(request, 'add-student.html', {'form': fm})

class Delete_student(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        studata = student.objects.get(id=id)
        studata.delete()
        return redirect('home1')

class Editstudent(View):
    def get(self, request, id):
        stu = student.objects.get(id=id)
        fm = AddstudentForm(instance=stu)
        return render(request, 'edit-student.html', {'form': fm})

    def post(self, request, id):
        stu = student.objects.get(id=id)
        fm = AddstudentForm(request.POST, instance=stu)
        if fm.is_valid():
            fm.save()
        return redirect('home1')
    

    