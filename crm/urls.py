from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'crm'


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('common.urls', namespace='common')),
    url(r'^', include('questions.urls', namespace='questions')),
    url(r'^knowledgebase/', include('knowledge_base.urls', namespace='knowledgebase')),
    url(r'^logout/$', views.logout, {'next_page': '/login/'}, name='logout'),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^tinymce/', include('tinymce.urls')),



]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
