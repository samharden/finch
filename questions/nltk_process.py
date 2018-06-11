'''
Uses NLTK to get the word frequency of the question and any comments associated
with the question, then searches for related questions and comments based on
the most frequently used words.
'''

import nltk
from nltk.corpus import stopwords, wordnet
from questions.models import Case, RelatedQuestions
from common.models import Comment
from django.shortcuts import render, get_object_or_404

def nltk_process(total_text, case_id):

    tokens = [t for t in total_text.split()]
    clean_tokens = tokens[:]

    for token in tokens:
        # Need to remove 'I'
        if token in stopwords.words('english'):
            clean_tokens.remove(token)
        if token == 'I':
            clean_tokens.remove(token)

    freq = nltk.FreqDist(clean_tokens)
    rel_q_list_raw = []
    ## Find similar questions based on word and word synonymsfrequency
    for key,val in freq.items():
        if val > 2:
            print("Word found: ", key)
            synonyms = []
            to_add = [e.id for e in Case.objects.filter(title__contains=str(key))]
            to_add2 = [e.id for e in Case.objects.filter(issue_detail__contains=str(key))]
            to_add3 = [e.case_id for e in Comment.objects.filter(comment__contains=str(key))]
            rel_q_list_raw.append(to_add)
            rel_q_list_raw.append(to_add2)
            rel_q_list_raw.append(to_add3)
            for syn in wordnet.synsets(key):
                for lemma in syn.lemmas():
                    synonyms.append(lemma.name())
            print(synonyms)
            for add_syn in synonyms:
                to_add_syn = [e.id for e in Case.objects.filter(title__contains=str(add_syn))]
                to_add_syn2 = [e.id for e in Case.objects.filter(issue_detail__contains=str(add_syn))]
                to_add_syn3 = [e.case_id for e in Comment.objects.filter(comment__contains=str(add_syn))]
                rel_q_list_raw.append(to_add_syn)
                rel_q_list_raw.append(to_add_syn2)
                rel_q_list_raw.append(to_add_syn3)

    rel_q_list_final = []
    for q_list in rel_q_list_raw:
        for x in q_list:
            # Need to remove repeats
            if int(x) != int(case_id) and x not in rel_q_list_final:
                rel_q_list_final.append(x)
    print(rel_q_list_final)
    return rel_q_list_final

def nltk_rel_words(total_text):
    synonyms = []
    tokens = [t for t in total_text.split()]
    clean_tokens = tokens[:]

    for token in tokens:
        # Need to remove 'I'
        if token in stopwords.words('english'):
            clean_tokens.remove(token)
        if token == 'I':
            clean_tokens.remove(token)
        if token == 'We':
            clean_tokens.remove(token)

    freq = nltk.FreqDist(clean_tokens)

    for key,val in freq.items():
        if val > 1:
            print("Word found: ", key)
            for syn in wordnet.synsets(key):
                for lemma in syn.lemmas():
                    synonyms.append(lemma.name())

    print(synonyms)
    return synonyms

def nltk_rel_words_email(total_text):
    synonyms = []
    tokens = [t for t in total_text.split()]
    clean_tokens = tokens[:]

    for token in tokens:
        # Need to remove 'I'
        if token in stopwords.words('english'):
            clean_tokens.remove(token)
        if token == 'I':
            clean_tokens.remove(token)
        if token == 'We':
            clean_tokens.remove(token)

    freq = nltk.FreqDist(clean_tokens)

    for key,val in freq.items():

        print("Word found: ", key)
        for syn in wordnet.synsets(key):
            for lemma in syn.lemmas():
                synonyms.append(lemma.name())

    return synonyms

'''
Need to have this run on chron, and update a model field for each quesiton with
a list of related questions
'''

def find_rel_questions(synonyms, area, jurisdiction, case_id):
    ## Find similar questions based on word and word synonymsfrequency
    rel_q = RelatedQuestions(question_id=case_id)
    rel_q.question_id = case_id
    rel_q.save()
    rel_q_list_raw = []
    for add_syn in synonyms:
        to_add_syn = [e.id for e in Case.objects.filter(
                                                        related_words__contains=str(add_syn)
                                                        ).filter(
                                                        county__contains=jurisdiction)]
        to_add_syn2 = [e.id for e in Case.objects.filter(title__contains=str(add_syn)
                                                        ).filter(
                                                        county__contains=jurisdiction)]

        rel_q_list_raw.append(to_add_syn)
        rel_q_list_raw.append(to_add_syn2)
    rel_q_list_final = []
    for q_list in rel_q_list_raw:
        for x in q_list:
            # Need to remove repeats
            if int(x) != int(case_id.id) and x not in rel_q_list_final:
                rel_q_list_final.append(x)
    print("NEW LIST =", rel_q_list_final)
    pre_rel_case = RelatedQuestions.objects.filter(question_id=case_id)
    pre_exist_list = []
    for help_me in pre_rel_case:
        for z in help_me.related_questions.all():
            print("Pre-Existing ID = ", z.id)
            pre_exist_list.append(z.id)
    print(pre_exist_list)
    for z in rel_q_list_final:
        print(z)
        add_rel_case = get_object_or_404(
            Case.objects.prefetch_related(), id=z)
        if z not in pre_exist_list:
            print("I'd add that")
            rel_q.related_questions.add(add_rel_case)

    rel_q.save()

def find_rel_questions_email(synonyms, area, jurisdiction):
    ## Find similar questions based on word and word synonymsfrequency
    rel_q = RelatedQuestions(question_id=case_id)
    rel_q.question_id = case_id
    rel_q.save()
    rel_q_list_raw = []
    for add_syn in synonyms:
        to_add_syn = [e.id for e in Case.objects.filter(
                                                        related_words__contains=str(add_syn)
                                                        ).filter(
                                                        county__contains=jurisdiction)]
        to_add_syn2 = [e.id for e in Case.objects.filter(title__contains=str(add_syn)
                                                        ).filter(
                                                        county__contains=jurisdiction)]

        rel_q_list_raw.append(to_add_syn)
        rel_q_list_raw.append(to_add_syn2)
    rel_q_list_final = []
    for q_list in rel_q_list_raw:
        for x in q_list:
            # Need to remove repeats
            if int(x) != int(case_id.id) and x not in rel_q_list_final:
                rel_q_list_final.append(x)
    print("NEW LIST =", rel_q_list_final)
    pre_rel_case = RelatedQuestions.objects.filter(question_id=case_id)
    pre_exist_list = []
    for help_me in pre_rel_case:
        for z in help_me.related_questions.all():
            print("Pre-Existing ID = ", z.id)
            pre_exist_list.append(z.id)
    print(pre_exist_list)
    for z in rel_q_list_final:
        print(z)
        add_rel_case = get_object_or_404(
            Case.objects.prefetch_related(), id=z)
        if z not in pre_exist_list:
            print("I'd add that")
            rel_q.related_questions.add(add_rel_case)

    rel_q.save()
