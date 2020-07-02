from django.shortcuts import render
from app.forms import *
# Create your views here.

def Topic(request):
    topicform=TopicForm()
    if request.method=='POST':
        form_data=TopicForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            
    return render(request,'topicform.html',context={'topicform':topicform})



