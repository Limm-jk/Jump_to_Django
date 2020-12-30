from django import forms
from pybo.models import Question, Answer


class QuestionForm(forms.ModelForm):
    # 모델 폼은 반드시 가져야함!
    # 사용할 모델과 필드를 저장
    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }
        
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }