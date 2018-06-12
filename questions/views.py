from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, reverse
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from questions.models import Case, UploadFile, RelatedQuestions
from questions.forms import CaseForm, CaseCommentForm, DocumentForm, CommentCommentForm
from common.models import User, Comment, Comment_2_Comment, Practicearea
from common.utils import PRIORITY_CHOICE, STATUS_CHOICE, INDCHOICES, body_plain as b_p
from common.utils import test_receive_email, determine_area, return_email_info
from itertools import chain
from questions.cite_finder import cite_finder
from django.db.models import F
from questions.cite_parse import link_grabber
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout, authenticate, login
from knowledge_base.models import KB_Item
import mammoth
import nltk
from nltk.corpus import stopwords
from questions.nltk_process import nltk_process, nltk_rel_words, find_rel_questions, nltk_rel_words_email, find_rel_questions_email
import talon

# CRUD Operations Start

@csrf_exempt
def login_crm(request):
    print('login')
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



@login_required
def user_profile_page(request, username):
    print(username)
    logged_in_user = request.user
    question_record = Case.objects.all()
    comments = Comment.objects.all()
    uploaded_docs = UploadFile.objects.all()
    user_record = get_object_or_404(
        User.objects.prefetch_related(), username=username)

    record = get_object_or_404(
        KB_Item.objects.prefetch_related(), statute_chapter=statute_chapter, KB_Item_number=KB_Item_number)


    user_record = User.objects.filter(username_contains=username)
    return render(request, "view_user.html", {
        'user_record': user_record,
        'logged_in_user': logged_in_user,
        'question_record':question_record,
        'comments':comments,
        'uploaded_docs':uploaded_docs,

    })

@login_required
def questions_list(request):
    questions = Case.objects.all().order_by('-score')
    page_title = 'Quorum'
    question_areas = Practicearea.objects.all().distinct()
    # question_areas = Case.objects.all().values_list('issue_area', flat=True).distinct()
    counties = Case.objects.all().values_list('county', flat=True).distinct()
    header = "Questions"
    page = request.POST.get('per_page')
    name = request.POST.get('name')
    specialty = request.POST.get('specialty')
    comments = Comment.objects.all()
    users = User.objects.all()
    state_filter = request.GET.get('state', '')
    area_filter = request.GET.get('area','')
    county_filter = request.GET.get('county','')
    searched = False
    KB_Items = KB_Item.objects.all().values_list('statute_chapter', flat=True).distinct()
    KB_Items_2 = KB_Item.objects.all()

    if len(state_filter) != 0:
        questions = Case.objects.filter(state__contains=state_filter)
        header = 'Questions in '+state_filter

    if len(area_filter) != 0:
        questions = Case.objects.filter(issue_area=area_filter)
        new_area = get_object_or_404(
            Practicearea.objects.prefetch_related(), id=area_filter).area
        header = 'Questions in ' + new_area
        print(header)


    if len(county_filter) != 0:
        questions = Case.objects.filter(county__contains=county_filter)
        header = 'Questions in '+county_filter
    if name:
        questions1 = Case.objects.filter(title__contains=name)
        questions2 = Case.objects.filter(issue_detail__contains=name)
        questions3 = Case.objects.filter(issue_summary__contains=name)
        questions4 = Case.objects.filter(state__contains=name)
        questions5 = Case.objects.filter(county__contains=name)
        questions6 = Case.objects.filter(related_doc_body__contains=name)
        questions7 = Case.objects.filter(related_words__contains=name)

        questions_raw = list(
                                chain(
                                        questions1,
                                        questions2,
                                        questions3,
                                        questions4,
                                        questions5,
                                        questions6,
                                        questions7)
                                    )
        questions=[]
        for add_question in questions_raw:
            if add_question not in questions:
                questions.append(add_question)



        searched = True

    score_up = request.GET.get('score_up','')
    if len(score_up) != 0:
        print("Score Up!", score_up)
        Case.objects.filter(id=score_up).update(score=F('score') + 1)
        User.objects.filter(email=Case.objects.get(id=score_up).created_by).update(score=F('score') + 1)
        return redirect("/")

    score_down = request.GET.get('score_down','')
    if len(score_down) != 0:
        if int(Case.objects.get(id=score_down).score) > 0:
            Case.objects.filter(id=score_down).update(score=F('score') - 1)
            print("Hey ", Case.objects.get(id=score_down).created_by, " your question got down-voted")
            ## Penalize the quesiton asker
            User.objects.filter(email=Case.objects.get(id=score_down).created_by).update(score=F('score') - 1)
            ##email notification function here
            return redirect("/")

    return render(request, "questions/list.html", {
        'questions': questions,
        'area_filter': area_filter,
        'state_filter':state_filter,
        'county_filter':county_filter,
        'question_areas': question_areas,
        'per_page': page,
        'header': header,
        'comments':comments,
        'users':users,
        'searched':searched,
        'name':name,
        'counties':counties,
        'KB_Items':KB_Items,
        'KB_Items_2':KB_Items_2,
        'page_title':page_title,
    })


@login_required
def add_question(request):
    users = User.objects.filter(is_active=True).order_by('email')
    form = CaseForm()
    page_title = 'Start Discussion'
    if request.method == 'POST':
        form = CaseForm(request.POST, request.FILES)

        if form.is_valid():
            case = form.save(commit=False)
            case.created_by = str(request.user)
            ## Fastcase
            if len(case.related_cite) != 0:
                case.related_cite_link = link_grabber(case.related_cite)

            case.score = 0
            state = request.user.state
            case.state = request.user.state
            case.county = request.user.county
            question_text = case.issue_detail
            case.related_words = nltk_rel_words(question_text)
            User.objects.filter(id=request.user.id).update(score=F('score') + 1)
            case.save()

            if case.related_document:
                User.objects.filter(id=request.user.id).update(score=F('score') + 4)

                ##need to pull pdf text

                if str(case.related_document).split('.')[1] == 'docx':
                    print("Word doc!")
                    with open("media/"+str(case.related_document).replace(" ", "_"),
                                "rb") as docx_file:
                        result = mammoth.convert_to_html(docx_file)
                        html = result.value # The generated HTML
                    print(html)
                    case.related_doc_body = html
                    case.created_by = str(request.user)

            case.save()

            if request.is_ajax():
                return JsonResponse({'error': False})
            if request.POST.get("savenewform"):
                return redirect("questions:case_add")
            else:
                # return HttpResponseRedirect(reverse('questions:list'))
                return HttpResponseRedirect("/"+str(case.id)+"/viewquestion")
        else:
            if request.is_ajax():
                return JsonResponse({'error': True, 'case_errors': form.errors})
            return render(request, "questions/create_questions.html", {
                'case_form': form,
                'users': users,
                'case_types': INDCHOICES,
                'case_priority': PRIORITY_CHOICE,
                'case_status': STATUS_CHOICE,
            })
    return render(request, "questions/create_questions.html", {
        'case_form': form,
        'users': users,
        'case_types': INDCHOICES,
        'case_priority': PRIORITY_CHOICE,
        'case_status': STATUS_CHOICE,
        'page_title':page_title,
    })


@login_required
def view_question(request, case_id):
    questions = Case.objects.all().order_by('-score')
    case_record = get_object_or_404(
        Case.objects.prefetch_related(), id=case_id)
    comments = case_record.questions.all().order_by('-score')
    related_comments = Comment.objects.filter( case_id=case_id)
    total_text = case_record.title + " " + case_record.issue_detail
    for rel_com in related_comments:
        total_text = total_text + " "+rel_com.comment
    rel_q_list_final = ""
    print(RelatedQuestions.related_questions)
    results_x = RelatedQuestions.objects.filter(question_id=case_record)
    text_to_send = case_record.related_words+" "+total_text
    rel_q_list_final = RelatedQuestions.objects.filter(question_id=case_record).count()
    print("Count =", rel_q_list_final)
    if rel_q_list_final>99:
        print("don't need to process it")
    else:
        find_rel_questions(
                            text_to_send,
                            case_record.issue_area,
                            case_record.county,
                            case_record
                            )

    if request.method == 'POST':
        comment_id = get_object_or_404(Comment, id=request.POST.get('commentid'))
        commenter = comment_id.commented_by_id
        comment_id_email = get_object_or_404(User, id=commenter).email
        print("Need to email ", comment_id_email)
        if request.user:
            form = CommentCommentForm(request.POST, request.FILES)
            if form.is_valid():
                comment_comment = form.save(commit=False)
                print(comment_comment.comment)
                #increment commenter score by 1
                User.objects.filter(id=request.user.id).update(score=F('score') + 1)
                comment_comment.comment = request.POST.get('comment')
                comment_comment.case_id_id = request.POST.get("case_id_id")
                comment_comment.commented_by = request.user
                comment_comment.orig_comment = comment_id
                print(comment_comment.commented_on)
                comment_comment.save()
        else:
            data = {'error': "You Dont Have permission to Comment"}
            return JsonResponse(data)

    if case_record.related_document:
        if str(case_record.related_document).split('.')[1] == 'pdf':
            pdf_odj = True
        else:
            pdf_odj = False
    else:
        pdf_odj = False
    comments = case_record.questions.all().order_by('-score')
    comments_2_comments = Comment_2_Comment.objects.filter(case_id_id=case_id)
    page_title = 'Quorum'
    KB_Items = KB_Item.objects.all().values_list('statute_chapter', flat=True).distinct()
    KB_Items_2 = KB_Item.objects.all()
    comment_score_up = request.GET.get('comment_score_up','')
    if len(comment_score_up) != 0:
        print("Comment Score Up!", comment_score_up)
        Comment.objects.filter(id=comment_score_up).update(score=F('score') + 1)
        User.objects.filter(id=Comment.objects.get(id=comment_score_up).commented_by_id).update(score=F('score') + 1)
        return redirect("/%s/viewquestion" % case_id)

    comment_score_down = request.GET.get('comment_score_down','')
    if len(comment_score_down) != 0:
        if int(Comment.objects.get(id=comment_score_down).score) > 0:
            print("Comment Score Down!", comment_score_down)
            Comment.objects.filter(id=comment_score_down).update(score=F('score') - 1)
            User.objects.filter(id=Comment.objects.get(id=comment_score_down).commented_by_id).update(score=F('score') - 1)
            return redirect("/%s/viewquestion" % case_id)

    logged_in_user = request.user
    users = User.objects.all()
    score_up = request.GET.get('score_up','')
    if len(score_up) != 0:
        print("Score Up!", score_up)
        Case.objects.filter(id=score_up).update(score=F('score') + 1)
        User.objects.filter(email=Case.objects.get(id=score_up).created_by).update(score=F('score') + 1)
        return redirect("/%s/viewquestion" % case_id)


    score_down = request.GET.get('score_down','')
    if len(score_down) != 0:
        if int(Case.objects.get(id=score_down).score) > 0:
            Case.objects.filter(id=score_down).update(score=F('score') - 1)
            print("Hey ", Case.objects.get(id=score_down).created_by, " your question got down-voted")
            ## Penalize the quesiton asker
            User.objects.filter(email=Case.objects.get(id=score_down).created_by).update(score=F('score') - 1)
            ##email notification function here
            return redirect("/%s/viewquestion" % case_id)

    return render(request, "questions/view_case.html", {
        'case_record': case_record,
        'comments': comments,
        'users':users,
        'logged_in_user':logged_in_user,
        'KB_Items':KB_Items,
        'KB_Items_2':KB_Items_2,
        'page_title':page_title,
        'pdf_odj':pdf_odj,
        'comments_2_comments':comments_2_comments,
        'rel_q_list_final':rel_q_list_final,
        'questions':questions,
        'results_x':results_x,
    })


@login_required
def edit_case(request, case_id):
    case_object = get_object_or_404(Case, id=case_id)
    users = User.objects.filter(is_active=True).order_by('email')
    form = CaseForm(instance=case_object)
    page_title = 'Edit Question'

    if request.method == 'POST':

        form = CaseForm(
            request.POST, request.FILES, instance=case_object)
        if form.is_valid():
            case_obj = form.save(commit=False)
            if request.POST.get("account"):
                case_obj.account = Account.objects.get(id=request.POST.get("account"))
            case_obj.created_by = str(request.user)
            case_obj.save()

            if request.is_ajax():
                return JsonResponse({'error': False})
            return HttpResponseRedirect(reverse('questions:list'))
        else:
            if request.is_ajax():
                return JsonResponse({'error': True, 'case_errors': form.errors})
            return render(request, "questions/create_questions.html", {
                'case_obj': case_object,
                'case_form': form,
                'users': users,
                'case_types': INDCHOICES,
                'case_priority': PRIORITY_CHOICE,
                'case_status': STATUS_CHOICE,
                'page_title':page_title,

            })

    return render(request, "questions/create_questions.html", {
        'case_form': form,
        'case_obj': case_object,
        'users': users,
        'case_types': INDCHOICES,
        'case_priority': PRIORITY_CHOICE,
        'case_status': STATUS_CHOICE,
        'page_title':page_title,


    })


@login_required
def remove_case(request, case_id):
    if request.method == 'POST':
        cid = request.POST['case_id']
        get_object_or_404(Case, id=cid).delete()
        count = Case.objects.filter(Q(assigned_to=request.user) | Q(created_by=request.user)).count()
        data = {"case_id": cid, "count": count}
        return JsonResponse(data)
    else:
        Case.objects.filter(id=case_id).delete()
        return HttpResponseRedirect(reverse('questions:list'))


# CRUD Operations End
# Comments Section Start


@login_required
def add_comment(request):
    print("HEY")
    if request.method == 'POST':
        case = get_object_or_404(Case, id=request.POST.get('caseid'))
        questioner_email = case.created_by
        print("Need to email ", questioner_email)
        ## Email notification that question got answered
        if request.user:
            form = CaseCommentForm(request.POST, request.FILES)
            if form.is_valid():
                case_comment = form.save(commit=False)

                #increment commenter score by 1
                User.objects.filter(id=request.user.id).update(score=F('score') + 1)
                case_comment.comment = request.POST.get('comment')
                case_comment.related_document = request.FILES.get('file_upload')

                case_comment.commented_by = request.user
                case_comment.case = case
                print("Orig Q =", case.issue_detail)
                case.related_words = nltk_rel_words(case.issue_detail+" "+case_comment.comment)
                case.save()
                case_comment.save()
                data = {"comment_id": case_comment.id, "comment": case_comment.comment,
                        "commented_on": case_comment.commented_on,
                        "commented_by": case_comment.commented_by.email}
                return JsonResponse(data)
            else:
                return JsonResponse({"error": form['comment'].errors})
        else:
            data = {'error': "You Dont Have permission to Comment"}
            return JsonResponse(data)



@login_required
def edit_comment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        comment_id = request.POST.get("commentid")
        comment_obj = get_object_or_404(Comment, id=comment_id)
        form = CaseCommentForm(request.POST)
        if request.user == comment_obj.commented_by:
            if form.is_valid():
                comment_obj.comment = comment
                comment_obj.save()
                data = {"comment": comment_obj.comment, "commentid": comment_id}
                return JsonResponse(data)
            else:
                return JsonResponse({"error": form['comment'].errors})
        else:
            return JsonResponse({"error": "You dont have authentication to edit"})
    else:
        return render(request, "404.html")


@login_required
def remove_comment(request):
    if request.method == 'POST':
        comment_id = request.POST.get('comment_id')
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user == comment.commented_by:
            comment.delete()
            data = {"cid": comment_id}
            return JsonResponse(data)
        else:
            return JsonResponse({"error": "You Dont have permisions to delete"})
    else:
        return HttpResponse("Something Went Wrong")

@login_required
def upload_file(request):
    users = User.objects.filter(is_active=True).order_by('email')
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            doc = form.save(commit=False)
            doc.created_by = request.user
            doc.save()

            if doc.document:

                if str(doc.document).split('.')[1] == 'docx':

                    print(doc.document)
                    with open("media/"+str(doc.document).replace(" ", "_"),
                                "rb") as docx_file:
                        result = mammoth.convert_to_html(docx_file)
                        html = result.value # The generated HTML
                    print(html)
                    doc.created_by = str(request.user)
                    doc.doc_body = html
                doc.save()

    else:
        form = DocumentForm()


    return render(request, "upload_file.html", {'form':form,})


@csrf_exempt
def receive_email(request):

    # test_receive_email(b_p)
    sender = 'sam@lancorp.co'
    recipient = 'appeals@mg.finch-km.com'
    subject = 'Test this thang fool'
    # return_email_info(sender, recipient, subject)

    if request.method == 'POST':
        talon.init()
        from talon import signature
        sender    = request.POST.get('sender')
        recipient = request.POST.get('recipient')
        subject   = request.POST.get('subject', '')
        body_plain = request.POST.get('body-plain', '')
        text, signature = signature.extract(body_plain, sender=sender)
        body_without_quotes = request.POST.get('stripped-text', '')
        sender_name = get_object_or_404(
        User.objects.prefetch_related(), email=sender)
        raw_sender_name = sender_name.username
        synonyms = nltk_rel_words_email(subject + " " + text)
        print("Synonyms = ", synonyms)

        to_save = Case(
                        state = sender_name.state,
                        county = sender_name.county,
                        title = subject,
                        issue_detail = text,
                        created_by = str(raw_sender_name),
                        issue_area_id = determine_area(recipient),
                        )
        to_save.save()
        print(to_save.id)

        return_email_info(sender, recipient, subject)

        find_rel_questions_email(
                            synonyms,
                            determine_area(recipient),
                            sender_name.county,
                            to_save.id)

        print("++++++++++++++++++++++++++++++++")
        print(raw_sender_name)
        print(subject)
        print("SUCCESS")
    #          # attachments:
    #     for key in request.FILES:
    #         file = request.FILES[key]
    #              # do something with the file
    #
    #      # Returned text is ignored but HTTP status code matters:
    #      # Mailgun wants to see 2xx, otherwise it will make another attempt in 5 minutes
    return HttpResponse('OK')
