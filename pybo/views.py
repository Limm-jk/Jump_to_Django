from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone

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

def detail(request, question_id):
    # 내용 출력
    question = get_object_or_404(Question, pk = question_id)
    context = {'question' : question}
    
    return render(request, 'pybo/question_detail.html', context)

def question_create(request):
    """
    pybo 질문등록
    """
    # 값의 유무를 확인해서 나눈 것이 아니야!
    # POST로 왔는지 GET으로 왔는지
    # 같은 url에서 다양하게 처리될 수 있지.
    
    # POST로 왔다면, 이것은 저장하기를 눌렀다는 의미!
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            # 디비에서 commit이 뭐지? 트랜잭션의 반영을 의미하지.
            # 비슷해! False로 해서 임시로 저장하겠음
            # 왜 임시로 했을까?
            # post로 받은 form에 결측치가 있잖아! date!
            question = form.save(commit=False)
            question.create_date = timezone.now()
            
            # 결측치 메꾼 후 save
            question.save()
            
            return redirect('pybo:index')
        
    else:
        form = QuestionForm()
        
    # GET이면 여기로 오지. 근데 값이 invalid해도 여기로 와. save를 안한다는 의미지
    context = {'form' : form}
    return render(request, 'pybo/question_form.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    
    # answer set은 fk로 선언하면서 생성됨
    # 여기의 request는 id가 넘어온다. post기 때문
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    
    return redirect('pybo:detail', question_id=question.id)