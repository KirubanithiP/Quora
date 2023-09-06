# project/urls.py
from django.urls import path, include
from django.views.generic import RedirectView
from . import views 
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='view_questions', permanent=False)),
    path('register/', views.register, name='register'), 
    path('login/', views.login, name='login'), 
    path('post_question/', views.post_question, name='post_question'),  
    path('answer_question/', views.answer_question, name='answer_question'), 
    path('view_questions/', views.view_questions, name='view_questions'),  
    path('like_answer/', views.like_answer, name='like_answer'), 
]
