from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    # Config의 url
    path('', views.index),
    path('<int:question_id>/', views.detail),
    path('question/create/', views.question_create, name='question_create'),
]