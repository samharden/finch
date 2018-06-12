from django.utils.translation import ugettext_lazy as _

def test_receive_email(body_plain):
    print("Test!")
    talon.init()
    from talon import signature
    sender    = 'sam@lancorp.co'
    subject   = "Motion to Suppress Evidence"

    text, signature = signature.extract(body_plain, sender=sender)
    print(text)
    body_without_quotes = request.POST.get('stripped-text', '')
    text_total = subject + " " + text
    # find_rel_questions_email(
    #                     text_total,
    #                     issue_area,
    #                     case_record.county,
    #                     )

    synonyms = nltk_rel_words_email(text_total)
    # determine frequency of issue areas in synonyms
    areas_list = Practicearea.objects.all()
    for what in areas_list:
        print(what)
        if str(what).lower() in synonyms:
            print("Matched ", what)
    print("Synonyms = ", synonyms)



body_plain = """
                Does anyone have a motion to suppress evidence for a
                DUI breathalyzer exam performed without knowing consent?


                Thanks,

                Sam Harden
                sam@lancorp.co
                lancorp.co"""


INDCHOICES = (
    ('CRIMINAL', 'CRIMINAL'),
    ('CIVIL NEGLIGENCE', 'CIVIL NEGLIGENCE'),
    ('FAMILY', 'FAMILY'),
    ('CIVIL OTHER', 'CIVIL OTHER')
)

CASE_TYPE = (

    ('GENERAL', 'GENERAL'),
    ('COMPLAINT', 'COMPLAINT'),
    ('ANSWER', 'ANSWER'),
    ('AFFIRMATIVE DEFENSES','AFFIRMATIVE DEFENSES'),
    ('COURT PROCEDURE', 'COURT PROCEDURE'),
    ('JUDGE PREFERENCE', 'JUDGE PREFERENCE'),

)

CRIM_CASE_TYPE_DETAIL = (
    ('FOURTH AMENDMENT', 'FOURTH AMENDMENT'),
    ('BOND', 'BOND'),
    ('TRIAL', 'TRIAL'),
    ('EXPERT', 'EXPERT'),
    ('STATUTORY CONSTRUCTION', 'STATUTORY CONSTRUCTION'),
    ('APPEAL', 'APPEAL'),
    ('FIFTH AMENDMENT', 'FIFTH AMENDMENT'),
)

# KB_TYPE = (
#     ('statute', 'Statute'),
#     ('case law', 'Case Law'),
#     ('memo', 'Memo'),
#     ('element', 'Element'),
# )

KB_TYPE = (
    ('guide','Practice Guide'),
    ('statute', 'Statute'),
    ('element', 'Element'),
    ('grounds', 'Grounds'),


)

RESULT_CHOICE = (
    ('SETTLED','SETTLED'),
    ('DISMISSED','DISMISSED'),
    ('ABANDONED','ABANDONED'),

)


STATUS_CHOICE = (
    ("Pre-Suit", "Pre-Suit"),
    ('Litigation', 'Litigation'),
    ('Appeal', 'Appeal'),
    ('Closed', 'Closed'),
    ('Rejected', 'Rejected'),

)

PRIORITY_CHOICE = (
    ("Low", "Low"),
    ('Normal', 'Normal'),
    ('High', 'High'),
    ('Urgent', 'Urgent')
)



COUNTIES = (
    ('Hillsborough', 'Hillsborough'),
)

STATES = (
    ('AL','AL'),
    ('CA','CA'),
    ('FL','FL'),
    ('GA','GA'),
    ('KY', 'KY'),
    ('IL','IL'),
    ('MS','MS'),
    ('NY','NY'),
    ('NC','NC'),
    ('SC','SC'),
    ('TN','TN'),
    ('TX','TX'),

)
