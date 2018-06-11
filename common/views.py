from django.core.files.uploadedfile import UploadedFile
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
# from common.forms import DocumentForm
from questions.models import Case, UploadFile
# from judges.models import Judges
from common.models import User, Comment
from common.forms import UserForm, SignUpForm
from django.contrib.auth.forms import PasswordChangeForm
# import textract
import os
from itertools import chain
from django.contrib.auth import get_user_model
User = get_user_model()

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect("/user/"+username+"/edit")
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def home(request):
    name = request.POST.get('name')
    current_user = request.user
    user_name = current_user.username
    state = current_user.state
    county = current_user.county
    results_num = 0
    show = False
    questions = False
    comments = Comment.objects.all()
    if name:
        questions1 = Case.objects.filter(title__contains=name)
        questions2 = Case.objects.filter(issue_detail__contains=name)
        questions3 = Case.objects.filter(issue_summary__contains=name)
        questions4 = Case.objects.filter(state__contains=name)
        questions5 = Case.objects.filter(county__contains=name)
        questions = list(chain(questions1, questions2, questions3, questions4, questions5))
        results_num = len(questions)

        show = True

    return render(request, 'index.html', {
                    'questions':questions,
                    'show':show,
                    'results_num':results_num,
                    'user_name':user_name,
                    'juris': county+state,
                    'comments':comments
                    } )


@csrf_exempt
def login_crm(request):
    print('login 1')
    if request.method == 'POST':
        print("POST")
        user = authenticate(username=request.POST.get('email'), password=request.POST.get('password'))
        print(user)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    return render(request, 'login.html')



# @login_required
def user_profile_page(request, username):
    print(username)
    page_title = "Profile"
    logged_in_user = request.user
    question_record = Case.objects.all()
    uploaded_docs = UploadFile.objects.all()
    comments = Comment.objects.all()
    user_record = get_object_or_404(
        User.objects.prefetch_related(), username=username)

    return render(request, "view_user.html", {
        'user_record': user_record,
        'logged_in_user': logged_in_user,
        'question_record':question_record,
        'comments':comments,
        'page_title':page_title,
        'uploaded_docs':uploaded_docs,

    })

@login_required
def edit_user(request, username):
    logged_in_user = request.user

    if str(logged_in_user) == username:
        user_record = get_object_or_404(
            User.objects.prefetch_related(), username=username)
        page_title = 'Edit Profile'
        form = UserForm(instance=user_record)

        if request.method == 'POST':
            form = UserForm(
                request.POST, instance=user_record)
            if form.is_valid():
                user_obj = form.save(commit=False)
                user_obj.save()
                return HttpResponseRedirect("/user/"+username+"/view")

        return render(request, "edit-user.html", {
                    'form': form,
                    'page_title':page_title,

                })
    else:
        page_title = "Sorry"
        return render(request, "edit-user.html", {
            'page_title':page_title,
        })

@login_required
def upload_file(request):

    users = User.objects.filter(is_active=True).order_by('email')
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    else:
        form = DocumentForm()


    return render(request, "upload_file.html", {'form':form,})
