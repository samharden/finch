from django.utils.translation import ugettext_lazy as _
import requests
from common.email_content import email_body
from common.email_content_comment import email_body_comment
from common.email_content_new import email_body_new
from crm.settings import DOMAIN_ROOT, MAILGUN_API_KEY


import re
def determine_area(recipient):
    if recipient == 'experts@'+DOMAIN_ROOT:
        issue_area_id_num = 5
    elif recipient == 'judges@'+DOMAIN_ROOT:
        issue_area_id_num = 4
    elif recipient == 'motions@'+DOMAIN_ROOT:
        issue_area_id_num = 3
    elif recipient == 'orders@'+DOMAIN_ROOT:
        issue_area_id_num = 2
    elif recipient == 'appeals@'+DOMAIN_ROOT:
        issue_area_id_num = 1
    elif recipient == 'pleadings@'+DOMAIN_ROOT:
        issue_area_id_num = 7
    else:
        if 'comment-alert' in recipient:
            case_id = re.findall('(\d+)', recipient)
            talon.init()
            from talon import signature
            sender = request.POST.get('sender')
            body_plain = request.POST.get('body-plain', '')
            text, signature = signature.extract(body_plain, sender=sender)
            sender_name = get_object_or_404(
            User.objects.prefetch_related(), email=sender)

            to_save = Comment_2_Comment(
                            orig_comment = 0,
                            case_id = case_id,
                            comment = text,
                            commented_by = sender_name,
                            )
            to_save.save()

        else:
            issue_area_id_num = 6
    return issue_area_id_num


def return_email_info(sender, recipient, subject, new_id):
    print("Emailing")
    return requests.post(
        "https://api.mailgun.net/v3/"+DOMAIN_ROOT+"/messages",
        auth=("api", MAILGUN_API_KEY),
        data={
                    "from": recipient,
                    "to": sender,

                    "subject": subject,

                    "html": email_body.format('http://'+DOMAIN_ROOT+str(new_id)+'/viewquestion/'),

                }
                )

def new_post_email_info(sender, recipient, subject, area, poster, body, new_id):
    print("Emailing")
    return requests.post(
        "https://api.mailgun.net/v3/"+DOMAIN_ROOT+"/messages",
        auth=("api", MAILGUN_API_KEY),
        data={
                    "from": sender,
                    "to": recipient,

                    "subject": subject,

                    "html": email_body_new.format(
                                area,
                                poster,
                                body,
                                'http://'+DOMAIN_ROOT+str(new_id)+'/viewquestion/'),

                }
                )


def return_email_info_comment(sender, recipient, subject, commenter, comment, new_id):
    print("Emailing")
    return requests.post(
        "https://api.mailgun.net/v3/"+DOMAIN_ROOT+"/messages",
        auth=("api", MAILGUN_API_KEY),
        data={
                    "from": recipient,
                    "to": sender,

                    "subject": subject,

                    "html": email_body_comment.format(
                                commenter,
                                comment,
                                'http://'+DOMAIN_ROOT+str(new_id)+'/viewquestion/',

                                ),

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
