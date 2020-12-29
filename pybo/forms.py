from django import forms
from pybo.models import Question


class QuestionForm(forms.ModelForm):
    # 모델 폼은 반드시 가져야함!
    # 사용할 모델과 필드를 저장
    class Meta:
        model = Question
        fields = ['subject', 'content']