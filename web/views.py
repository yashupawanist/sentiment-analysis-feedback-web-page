from django.shortcuts import render, redirect
from .models import registration

# Create your views here.
def index(request):
    return render(request,'index.html')
def portfolio(request):
    return render(request,'portfolio.html')
def features(request):
    return render(request,'features.html')
def contact(request):
    return render(request,'contact.html')
def index1(request):
    return render(request,'index1.html')
def logout(request):
    return render(request, 'signup.html')

'''
def feedback_list(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedback_list.html', {'feedbacks': feedbacks}) '''
