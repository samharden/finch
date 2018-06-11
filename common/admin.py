from django.contrib import admin
from common.models import User, Comment, Comment_Files, Casetype, Practicearea, KBType
# Register your models here.

admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Comment_Files)
admin.site.register(Casetype)
admin.site.register(Practicearea)
admin.site.register(KBType)
# admin.site.register(UploadFileCommon)
