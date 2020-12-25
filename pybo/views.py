from django.shortcuts import render
from django.http import HttpResponse
from .forms import QuestionForm


def index(request):
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")

def question_create(request):
    """
    pybo 질문등록
    """
    form = QuestionForm()
    return render(request, 'pybo/question_form.html', {'form': form})