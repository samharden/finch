from django.db import models
from django.forms import Textarea
from django.utils.translation import pgettext_lazy
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from common.models import User, Casetype, Practicearea, KBType
# from questions.models import Case
from common.utils import CASE_TYPE, COUNTIES, PRIORITY_CHOICE, STATUS_CHOICE, INDCHOICES, KB_TYPE, RESULT_CHOICE, STATES

class KB_Item(models.Model):
    # kb_type = models.CharField(pgettext_lazy("Type of Item", "Type of Item"), choices=KB_TYPE,  max_length=64)
    # kb_type = models.ForeignKey(KBType, on_delete=models.CASCADE)
    title = models.CharField(
        pgettext_lazy("Title", "Title"),
        max_length=64)
    citation = models.CharField(
        pgettext_lazy("Case Citation", "Case Citation"),
        max_length=64, default="")
    judge = models.CharField(
        pgettext_lazy("Judge", "Judge"),
        max_length=64, default="")
    statute_chapter = models.CharField(
        pgettext_lazy("Statute Chapter", "Statute Chapter"),
        max_length=64)
    statute_heading = models.CharField(
        pgettext_lazy("Heading", "Heading"),
        max_length=64)
    statute_number = models.CharField(
        pgettext_lazy("Statute Number", "Statute Number"),
        max_length=64)
    state = models.CharField(choices=STATES, max_length=64, default="FL")
    body = models.TextField(
        pgettext_lazy("HTML Body", "HTML Body"),
        max_length=60000, default="")
    plain_body = models.TextField(
        pgettext_lazy("Plain Body", "Plain Body"),
        max_length=60000,
        )
    trigger = models.CharField(
        pgettext_lazy("Trigger", "Trigger"),
        max_length=600, default="")
    aff_resp = models.CharField(
        pgettext_lazy("If Affirmate Response to Trigger", "If Affirmate Response to Trigger"),
        max_length=600, default="")
    neg_resp = models.CharField(
        pgettext_lazy("If Negative Response to Trigger", "If Negative Response to Trigger"),
        max_length=600, default="")
    kb_area = models.ForeignKey(Practicearea, on_delete=models.CASCADE)
    # kb_area = models.CharField(pgettext_lazy("Area", "Area"), choices=CASE_TYPE, max_length=64)

    class Meta:
        ordering = ['kb_area']
    def __str__(self):
        return self.title
        # if len(self.statute_chapter) > 0:
        #     return self.statute_heading + " " + self.statute_chapter+"."+self.statute_number+ " ("+ str(self.kb_type) +")"
        # else:
        #     return self.title + " " + "("+ self.kb_type +")"

class Document(models.Model):
    title = models.CharField(
        pgettext_lazy("Title", "Title"),
        max_length=64)
    practice_area = models.CharField(choices=CASE_TYPE, max_length=64)
    description = models.CharField(
        pgettext_lazy("Description", "Description"),
        max_length=300)
    body = models.CharField(
        pgettext_lazy("Body", "Body"),
        max_length=60000)

    def __str__(self):
        return self.title
