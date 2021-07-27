from django.shortcuts import render
from django.http import HttpResponse
from .models import QuestionManager, Question, Answer
from .forms import CreateNewQuestion
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db import connection, connections
from django.http import Http404


def index(request, *args, **kwargs):
    #ser_ip = request.META.get('HTTP_X_REAL_IP')
    # if user_ip in None:
    meta = request.META
    user = request.user
    session = request.session
    files = request.FILES
    cookies = request.COOKIES
    post = request.POST
    get = request.GET
    method = request.method
    # return HttpResponse(HTML, status=200)
    return render(request, 'test_template.html', {})
# Create your views here.


def new_questions(request, *args, **kwargs):
    #user = User.objects.create_user(username='Nikk', password='1234')
    # user.save()
    user = User.objects.get(username='Nikk')
    # q1 = Question(title='test_title_' + str(i), text='test_text_' + str(i),
    #              rating=8, author=user)
    # q1.save()
    # q2 = Question(title='test_title_' + str(i + 1), text='test_text_' + str(i + 1),
    #              rating=3, author=user)
    # q2.save()
    questions = Question.objects.new()
    return render(request, 'new_questions_template.html', {'questions': questions})


def popular_questions_list(request, *args, **kwargs):
    user = User.objects.get(username='Nikk')
    questions = Question.objects.popular()
    limit = 10
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)
    #answer = Answer(text='helllo!', question=questions[0], author=user)
    # answer.save()
    return render(request, 'popular_questions_template.html', {'paginator': paginator, 'questions': questions[(page.number - 1) * 10:page.number * 10]})


def new_questions_list(request, *args, **kwargs):
    user = User.objects.get(username='Nikk')
    questions = Question.objects.new()
    limit = 10
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/new/?page='
    page = paginator.page(page)
    #answer = Answer(text='helllo!', question=questions[0], author=user)
    # answer.save()
    return render(request, 'new_questions_template.html', {'paginator': paginator, 'questions': questions[(page.number - 1) * 10:page.number * 10]})


def single_question(request, id):
    try:
        question = Question.objects.get(id=id)
    except Question.DoesNotExist:
        return HttpResponse('<p><h1>Question does not exist</h1></p>', status=404)
    answers = Answer.objects.filter(question_id=id)
    return render(request, 'single_question_template.html', {'question': question, 'answers': answers})


def ask(request, *args, **kwargs):
    pass


def signup(request, *args, **kwargs):
    pass


def login(request, *args, **kwargs):
    pass


def create(request, *args, **kwargs):
    user = User.objects.get(username='Nikk')
    if request.method == 'POST':
        form = CreateNewQuestion(response.POST)

        if form.is_valid():
            new_title = form.cleaned_data["title"]
            new_text = form.cleaned_data["text"]
            new_rating = form.cleaned_data["rating"]
            new_q = Question(title=new_title, text=new_text,
                             rating=new_rating, author=user)
            t.save()
    form = CreateNewQuestion()
    return render(request, 'create.html', {'form': form})
