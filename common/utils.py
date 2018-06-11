from django.utils.translation import ugettext_lazy as _

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
