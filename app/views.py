from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
from app.forms import *

def student(request):
    form=StudentForm()
    if request.method=='POST':
        form_data=StudentForm(request.POST)
        if form_data.is_valid():
            name=form_data.cleaned_data['name']
            age=form_data.cleaned_data['age']
            pw=form_data.cleaned_data['password']
            ad=form_data.cleaned_data['address']
            gender=form_data.cleaned_data['gender']
            d={'name':name,'age':age,'pw':pw,'ad':ad,'gender':gender}
            return render(request,'student_formdata.html',d)
    return render(request,'student.html',context={'form':form})

def insert_topic(request):
    form=TopicForm()
    if request.method=='POST':
        form_data=TopicForm(request.POST)
        if form_data.is_valid():
            topicname=form_data.cleaned_data['topicname']
            t=Topic.objects.get_or_create(topic_name=topicname)[0]
            t.save()
            return HttpResponse('Data inserted Successfully')
    return render(request,'insert_topic.html',context={'form':form})