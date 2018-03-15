from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question
# Create your views here.
'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_data')[:5]
    print(latest_question_list)
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output) 
'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_data')[:5]
    template = loader.get_template('hello/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def reslult(request, querstion_id):
    response = "you,re looking at the reslult of quersion"+str(querstion_id)
    return HttpResponse(response)

def detail(request, querstion_id):
    response = "you,re looking at the detail of quersion" + str(querstion_id)
    return HttpResponse(response)

def vote(request,querstion_id):
    response = "you,re voting on quersion" + str(querstion_id)
    return HttpResponse(response)