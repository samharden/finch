from django.db import models
from django.forms import Textarea
from django.utils.translation import pgettext_lazy
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from common.models import User, LegalAidOrg
from common.utils import CASE_TYPE, PRIORITY_CHOICE, STATUS_CHOICE, INDCHOICES, KB_TYPE, RESULT_CHOICE
from tinymce.models import HTMLField
from knowledge_base.models import KB_Item, Practicearea


class Case(models.Model):
    title = models.CharField(
        pgettext_lazy("Question Title", "Question Title"),
        max_length=150)
    related_cite = models.CharField(max_length=64)
    related_cite_link = models.CharField(max_length=300)
    rel_statute_link = models.ForeignKey(KB_Item,
            on_delete=models.CASCADE,
            blank=True, null=True, related_name="case_number")

    issue_summary = models.CharField(
        pgettext_lazy("Summary", "Summary"),
        max_length=256)
    issue_detail = HTMLField()
    issue_area = models.ForeignKey(Practicearea, on_delete=models.CASCADE)
    # issue_area = models.CharField(choices=CASE_TYPE, max_length=255, blank=True, null=True, default='GENERAL')
    # created_by = models.CharField(max_length=76)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    related_document = models.FileField(upload_to='documents/')
    related_document_name = models.CharField(
        pgettext_lazy("Upload Name", "Upload Name"),
        max_length=64)
    related_document_desc = models.CharField(
        pgettext_lazy("Description", "Description"),
        max_length=64)
    related_doc_body = models.CharField(max_length=60000, default="")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=76)
    county = models.CharField(max_length=76)
    score = models.CharField(max_length=64)
    marked_as_inapprop = models.BooleanField(default=False)
    related_words = models.CharField(max_length=1000, default="")
    visible_to = models.ManyToManyField(LegalAidOrg, default="", blank=True)

    # class Meta:
    #     ordering = ['score']
    def __str__(self):
        return self.title

class RelatedQuestions(models.Model):
    question_id = models.ForeignKey(Case, on_delete=models.CASCADE, blank=True, null=True, related_name="case_number")
    related_questions = models.ManyToManyField(Case)


def user_directory_path(self, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(Case.objects.get(id=3), filename)


class UploadFile(models.Model):

    name = models.CharField(max_length=255)
    created_by = models.CharField(max_length=76)
    file_type = models.CharField(choices=KB_TYPE, max_length=64)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    doc_body = models.CharField(max_length=60000, default="")
    # document = models.FileField(upload_to='user_directory_path')
    uploaded_at = models.DateTimeField(auto_now_add=True)
