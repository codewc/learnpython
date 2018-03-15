from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.http import Http404
from django.urls import reverse


from django.template import loader
from .models import Question,Choice
# Create your views here.
'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_data')[:5]
    print(latest_question_list)
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output) 
'''

'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_data')[:5]
    template = loader.get_template('hello/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
'''

def index(request):
    latest_querstion_list = Question.objects.order_by('-pub_data')[:5]
    context = {'latest_question_list':latest_querstion_list}
    return render(request, 'hello/index.html', context)

def reslult(request, querstion_id):
    response = "you,re looking at the reslult of quersion"+str(querstion_id)
    return HttpResponse(response)
'''
def detail(request, querstion_id):
    response = "you,re looking at the detail of quersion" + str(querstion_id)
    return HttpResponse(response)

'''
def detail(request,querstion_id):
    try:
        question = Question.objects.get(pk=querstion_id)
    except Question.DoesNotExist:
        raise Http404('Querstion does not exist')
    context = {'question':question}
    return render(request, 'hello/detail.html', context)
'''
def vote(request,querstion_id):
    response = "you,re voting on quersion" + str(querstion_id)
    return HttpResponse(response)

'''

def vote(request, querstion_id):
    question = get_object_or_404(Question, pk=querstion_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'hello/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('hello:results', args=(question.id,)))