from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, reverse
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from questions.models import Case, UploadFile
from questions.forms import CaseForm, CaseCommentForm, DocumentForm
from common.models import User, Comment, KBType, Practicearea
from common.utils import PRIORITY_CHOICE, STATUS_CHOICE, INDCHOICES
from itertools import chain
from questions.cite_finder import cite_finder
from django.db.models import F
from questions.cite_parse import link_grabber
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout, authenticate, login
from knowledge_base.models import KB_Item
from knowledge_base.forms import KnowledgebaseForm
import mammoth
import nltk
from nltk.corpus import stopwords
from questions.nltk_process import nltk_process, nltk_rel_words, find_rel_questions
from django.core import serializers
from bs4 import BeautifulSoup as bsoup
# Create your views here.
@login_required
def knowledge_base_list(request):
    name = request.POST.get('name')
    state_filter = request.GET.get('state', '')
    questions = Case.objects.all()
    all_kb_items = KB_Item.objects.all()
    kb_areas = Practicearea.objects.all()
    # kb_areas = KBType.objects.all()

    states = KB_Item.objects.all().values_list('state', flat=True).distinct()
    # statutes = KB_Item.objects.all().values_list('statute_chapter', flat=True).distinct()
    statutes = KB_Item.objects.filter(kb_area=2).values_list('statute_chapter', 'state').distinct()
    # statutes_2 = KB_Item.objects.all()
    statutes_2 = KB_Item.objects.filter(kb_area=2).distinct()
    prac_guides = KB_Item.objects.filter(kb_area=1).distinct()
    elements = KB_Item.objects.filter(kb_area=4).distinct()
    grounds = KB_Item.objects.filter(kb_area=5).distinct()
    page_title = "Knowledge Base"
    if len(state_filter) != 0:
        statutes = KB_Item.objects.filter(kb_area__contains='statute').filter(state__contains=state_filter).values_list('statute_chapter', 'state').distinct()
        statutes_2 = KB_Item.objects.filter(kb_area__contains='statute').filter(state__contains=state_filter).distinct()
        prac_guides = KB_Item.objects.filter(kb_area__contains='guide').filter(state__contains=state_filter).distinct()
        elements = KB_Item.objects.filter(kb_area__contains='element').filter(state__contains=state_filter).distinct()
    if name:
        print(name)
        items_1 = KB_Item.objects.filter(statute_heading__contains=name)
        items_2 = KB_Item.objects.filter(body__contains=name)

        questions_raw = list(
                                chain(
                                        items_1,
                                        items_2,
                                        )
                            )
        print(questions_raw)
        statutes_2==[]
        for add_question in questions_raw:
            if add_question not in statutes_2:
                statutes_2.append(add_question.serialize())


        searched = True
        #
        # statutes_2 = list(chain(questions1, questions2))
        # searched = True

    return render(request, "knowledge_base/list2.html", {
    'statutes':statutes,
    'questions':questions,
    'statutes_2':statutes_2,
    'page_title':page_title,
    'prac_guides':prac_guides,
    'elements':elements,
    'states':states,
    'grounds':grounds,
    'all_kb_items':all_kb_items,
    'kb_areas':kb_areas,
    'kb_areas':kb_areas,
    })

@login_required
def knowledge_base_statute(request, statute_chapter, statute_number):
    print("HEYYYYY")
    statute = get_object_or_404(
        KB_Item.objects.prefetch_related(), statute_chapter=statute_chapter, statute_number=statute_number)
    print(statute)
    questions = Case.objects.filter(rel_statute_link=statute.id)
    form = CaseForm()
    page_title = "Knowledge Base"
    if request.method == 'POST':
        form = CaseForm(request.POST, request.FILES)

        if form.is_valid():
            case = form.save(commit=False)
            case.created_by = str(request.user)
            ## Fastcase
            if len(case.related_cite) != 0:
                case.rel_statute_link = link_grabber(case.related_cite)

            case.score = 0
            state = request.user.state
            case.state = request.user.state
            case.county = request.user.county
            case.rel_statute_link = statute
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
                return render(request, "knowledge_base/statute.html", {
                    'statute':statute,
                    'questions':questions,
                    })
        else:
            if request.is_ajax():
                return JsonResponse({'error': True, 'case_errors': form.errors})
            return render(request, "knowledge_base/statute.html", {
                'statute':statute,
                'questions':questions,
                })


    return render(request, "knowledge_base/statute.html", {
    'statute':statute,
    'questions':questions,
    'form':form,

    })




def statute_as_json(request, type, state, statute_chapter, statute_number):
    state = state.upper()
    ## Need to add plain text version to db, so don't have to clean it.
    ## Need way of storing elements in a structured format as well
        # Aff D available if X, Y, Z
        # Complaint requirements
        # Deadlines for filing answer
        #
    data = serializers.serialize(
                                'json',
                                KB_Item.objects.filter(
                                    kb_area__contains=type,
                                    state__contains=state,
                                    statute_chapter__contains=statute_chapter,
                                    statute_number__contains=statute_number,
                                    ),
                                    fields=('kb_area','state','statute_chapter','statute_number','plain_body')
                                )
    # soup = bsoup(data)
    # text = soup.get_text()

    return HttpResponse(data)

def element_as_json(request, type, state, kb_area, statute_heading):
    state = state.upper()
    data = serializers.serialize(
                                'json',
                                KB_Item.objects.filter(
                                    kb_area__contains=type,
                                    state__contains=state,
                                    
                                    statute_heading__contains=statute_heading,
                                    ),
                                    fields=('kb_area','state','kb_area','statute_heading','plain_body', 'trigger')
                                )

    return HttpResponse(data)

def all_element_as_json(request, type, state):
    state = state.upper()
    data = serializers.serialize(
                                'json',
                                KB_Item.objects.filter(
                                    kb_area__contains=type,
                                    state__contains=state,
                                    ),
                                    fields=('kb_area',
                                    'state',
                                    'kb_area',
                                    'statute_chapter',
                                    'statute_number',
                                    'statute_heading',
                                    'plain_body',
                                    'trigger')
                                )

    return HttpResponse(data)

@login_required
def knowledge_base_guide(request, kb_id):
    print("HEY:")
    # title = title.replace("-"," ")
    guide = get_object_or_404(
        KB_Item.objects.prefetch_related(), id=kb_id)

    questions = Case.objects.filter(rel_statute_link=guide.id)
    form = CaseForm()
    page_title = "Knowledge Base"
    if request.method == 'POST':
        form = CaseForm(request.POST, request.FILES)

        if form.is_valid():
            case = form.save(commit=False)
            case.created_by = str(request.user)
            ## Fastcase
            if len(case.related_cite) != 0:
                case.rel_statute_link = link_grabber(case.related_cite)

            case.score = 0
            state = request.user.state
            case.state = request.user.state
            case.county = request.user.county
            case.rel_statute_link = guide
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
                return render(request, "knowledge_base/statute.html", {
                    'guide':guide,
                    'questions':questions,
                    })
        else:
            if request.is_ajax():
                return JsonResponse({'error': True, 'case_errors': form.errors})
            return render(request, "knowledge_base/statute.html", {
                'guide':guide,
                'questions':questions,
                })


    return render(request, "knowledge_base/guide.html", {
    'guide':guide,
    'questions':questions,
    'form':form,

    })

@login_required
def knowledge_base_add(request):

    form = KnowledgebaseForm()
    page_title = "Knowledge Base"
    if request.method == 'POST':
        form = KnowledgebaseForm(request.POST, request.FILES)

        if form.is_valid():
            kb_item = form.save(commit=False)
            kb_item.created_by = str(request.user)
            ## Fastcase
            # if len(kb_item.related_cite) != 0:
            #     kb_item.rel_statute_link = link_grabber(case.related_cite)


            User.objects.filter(id=request.user.id).update(score=F('score') + 1)
            kb_item.save()



            if request.is_ajax():
                return JsonResponse({'error': False})
            if request.POST.get("savenewform"):
                return redirect("questions:case_add")
            else:
                return redirect("/knowledgebase")
        else:
            if request.is_ajax():
                return JsonResponse({'error': True, 'case_errors': form.errors})
            return redirect("knowledgebase")


    return render(request, "knowledge_base/add.html", {
    'form':form,

    })

@login_required
def view_knowledgebase(request, chapter, statute_number ):
    record = get_object_or_404(
        KB_Item.objects.prefetch_related(), chapter=chapter, statute_number=statute_number)
    statutes = KB_Item.objects.all().values_list('chapter', flat=True).distinct()
    statutes_2 = Statute.objects.all()
    questions = Case.objects.all()


    print(record)
    return render(request, "knowledge_base/view.html", {
        'case_record': record,
        'statutes': statutes,
        'statutes_2': statutes_2,
        'questions':questions,
    })
