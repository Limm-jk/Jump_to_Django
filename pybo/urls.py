from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    # Config의 url
    path('', views.index),
    # question의 id를 기준으로 조회
    path('<int:question_id>/', views.detail),
    path('question/create/', views.question_create, name='question_create'),
]