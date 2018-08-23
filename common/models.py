from django.db import models
from django.utils.translation import pgettext_lazy
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from common.utils import COUNTIES, KB_TYPE, CASE_TYPE, STATES
from tinymce.models import HTMLField

class LegalAidOrg(models.Model):
    name = models.CharField(pgettext_lazy("Name", "Name"), max_length=400)
    street_address = models.CharField(pgettext_lazy("Address", "Address"), max_length=1000)
    city = models.CharField(pgettext_lazy("City", "City"), max_length=500)
    state = models.CharField(pgettext_lazy("State", "State"), max_length=400)
    zip_code = models.CharField(pgettext_lazy("Zip", "Zip"), max_length=400)
    website_url = models.CharField(pgettext_lazy("Website", "Website"), max_length=1000)
    def __str__(self):
        return self.name

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(('date joined'), auto_now_add=True)
    state = models.CharField(choices=STATES, max_length=64)
    county = models.CharField(choices=COUNTIES, max_length=64)
    primary_practice_area = models.CharField(choices=CASE_TYPE, max_length=64)
    score = models.CharField(max_length=64, default=0)
    website = models.CharField(max_length=100, default='')
    ppa_percent = models.CharField(max_length=4, default='0')
    secondary_practice_area = models.CharField(choices=CASE_TYPE, max_length=64, default='NA')
    spa_percent = models.CharField(max_length=4, default='0')
    legal_aid_org = models.ForeignKey(LegalAidOrg, on_delete=models.CASCADE, blank=True, null=True)

    # USERNAME_FIELD = 'email'
    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['username',]
    REQUIRED_FIELDS = ['email',]

    objects = UserManager()

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.email



class Casetype(models.Model):
    type = models.CharField(pgettext_lazy("Area", "Area"),max_length=1000)

    def __str__(self):
        return self.type

class Practicearea(models.Model):
    area = models.CharField(pgettext_lazy("Area", "Area"), max_length=1000)

    def __str__(self):
        return self.area

class KBType(models.Model):
    kb_type = models.CharField(pgettext_lazy("Area", "Area"), max_length=1000)

    def __str__(self):
        return self.kb_type

class Comment(models.Model):
    case = models.ForeignKey('questions.Case', blank=True, null=True, related_name="questions", on_delete=models.CASCADE)
    # motion = models.ForeignKey('common.UploadFileCommon', blank=True, null=True, related_name="motions", on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    commented_on = models.DateTimeField(auto_now_add=True)
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    score = models.CharField(max_length=64, default=0)
    ##Need to add file upload
    related_document = models.FileField(upload_to='documents/')

    def get_files(self):
        return Comment_Files.objects.filter(comment_id=self)

class Comment_2_Comment(models.Model):
    orig_comment = models.ForeignKey('common.Comment', blank=True, null=True, related_name="comments", on_delete=models.CASCADE)
    case_id = models.ForeignKey('questions.Case', blank=True, null=True, related_name="case", on_delete=models.CASCADE)
    # motion = models.ForeignKey('common.UploadFileCommon', blank=True, null=True, related_name="motions", on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    commented_on = models.DateTimeField(auto_now_add=True)
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    score = models.CharField(max_length=64, default=0)



class Comment_Files(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now_add=True)
    comment_file = models.FileField("File", upload_to="comment_files", default='')

    def get_file_name(self):
        if self.comment_file:
            return self.comment_file.path.split('/')[-1]
        else:
            return None
