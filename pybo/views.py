from django.shortcuts import render
from django.http import HttpResponse

from .forms import QuestionForm
from .models import Question

def index(request):

    question_list = Question.objects.order_by('-create_date')
    # orderby는 어떤 것을 따라 정렬할 지 매개변수에 의해 결정
    # 매개변수의 -는 역순으로 정렬하겠음을 의미
    context = {'question_list' : question_list}

    # Request는 요청 값. 앞으로 세션 유저 등등 중요한 정보를 담을 것.
    # render_to_response(template_name, context=None, content_type=None, status=None, using=None)
    # 다양하게 쓰고 싶다면 context dict에 잔뜩 담아~~
    return render(request, 'pybo/question_list.html', context)

def question_create(request):
    """
    pybo 질문등록
    """
    form = QuestionForm()
    return render(request, 'pybo/question_form.html', {'form': form})