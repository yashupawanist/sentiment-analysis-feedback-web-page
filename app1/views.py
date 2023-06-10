from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from .models import Feedback
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
#from django.shortcuts import render, redirect
#from feedback.models import Feedback
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('index')

def submit_feedback(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        disease_effect = request.POST['disease-effect']
        symptoms = request.POST['symptoms']
        precautions = request.POST['precautions']
        course_duration = request.POST['Course_duration']

        feedback = Feedback(
            name=name,
            age=age,
            gender=gender,
            disease_effect=disease_effect,
            symptoms=symptoms,
            precautions=precautions,
            course_duration=course_duration
        )
        feedback.save()

        return redirect('feedback_success')  # Redirect to a success page
    else:
        return render(request, 'feedback.html')  # Render the form page initially


'''
def feedback_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        disease_effect = request.POST['disease-effect']
        symptoms = request.POST['symptoms']
        precautions = request.POST['precautions']

        feedback = Feedback(
            name=name,
            age=age,
            gender=gender,
            disease_effect=disease_effect,
            symptoms=symptoms,
            precautions=precautions
        )
        feedback.save()

        return redirect('feedback:feedback_list')

    return render(request, 'feedback/home.html')

def feedback_list(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedback/home.html', {'feedbacks': feedbacks})'''
