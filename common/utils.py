from django.utils.translation import ugettext_lazy as _
import requests
from common.email_content import email_body

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


def determine_area(recipient):
    if recipient == 'experts@mg.finch-km.com':
        issue_area_id_num = 5
    elif recipient == 'judges@mg.finch-km.com':
        issue_area_id_num = 4
    elif recipient == 'motions@mg.finch-km.com':
        issue_area_id_num = 3
    elif recipient == 'orders@mg.finch-km.com':
        issue_area_id_num = 2
    elif recipient == 'appeals@mg.finch-km.com':
        issue_area_id_num = 1
    else:
        issue_area_id_num = 6
    return issue_area_id_num


def return_email_info(sender, recipient, subject, new_id):
    return requests.post(
        "https://api.mailgun.net/v3/mg.finch-km.com/messages",
        auth=("api", "21aea2e8816a5714720bea94a065e953-b892f62e-45bfc044"),
        data={
                    "from": recipient,
                    "to": sender,

                    "subject": subject,

                    "html": email_body,

                }
                )


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
