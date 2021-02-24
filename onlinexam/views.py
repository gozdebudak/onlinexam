from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Exam

# Create your views here.
def detail(request, exam_id):
	exam = get_object_or_404(Exam, pk=exam_id)
	questions = Question.objects.all().filter(exam_id=exam_id)
	question_list = list(questions)
	return render(request, 'onlinexam/detail.html', {'exam': exam,'question_list': question_list})

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('onlinexam/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def expired(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    return render(request, 'onlinexam/expired.html', {'exam': exam})


def notStarted(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    return render(request, 'onlinexam/notStarted.html', {'exam': exam})