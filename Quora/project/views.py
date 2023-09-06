from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Question, Answer, Like
from .forms import QuestionForm, AnswerForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            
    else:
        form = UserCreationForm()
    return render(request, 'project/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            
        else:
            
            messages.error(request, 'Invalid username or password. Please try again.')
    return render(request, 'project/login.html')

@login_required
def post_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            
    else:
        form = QuestionForm()
    return render(request, 'project/post_question.html', {'form': form})

@login_required
def answer_question(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = question
            answer.save()
           
    else:
        form = AnswerForm()
    return render(request, 'project/answer_question.html', {'form': form, 'question': question})

@login_required
def view_questions(request):
    questions = Question.objects.all()
    return render(request, 'project/view_questions.html', {'questions': questions})


@login_required
def like_answer(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    like, created = Like.objects.get_or_create(user=request.user, answer=answer)
    if not created:
        like.delete()
   
