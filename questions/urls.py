from django.conf.urls import url
from questions import views

app_name = 'questions'


urlpatterns = [
    url(r'^$', views.questions_list, name='list'),
    url(r'^login/$', views.login_crm, name="home"),
    url(r'^create/$', views.add_question, name='add_question'),
    url(r'^upload_file/$', views.upload_file, name='upload_files'),
    url(r'^(?P<case_id>\d+)/viewquestion/$', views.view_question, name='view_case'),
    url(r'^(?P<case_id>\d+)/edit_quesiton/$', views.edit_case, name='edit_question'),
    url(r'^(?P<case_id>\d+)/remove/$', views.remove_case, name='remove_case'),
    # comments
    url(r'^comment/add/$', views.add_comment, name='add_comment'),
    # url(r'^comment2/add/$', views.add_comment_to_comment, name='add_2_comment'),
    url(r'^comment/edit/$', views.edit_comment, name='edit_comment'),
    url(r'^comment/remove/$', views.remove_comment, name='remove_comment'),
    url(r'^receive-email/$', views.receive_email, name='receive_email'),
]
