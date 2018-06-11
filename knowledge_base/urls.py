from django.conf.urls import url
from knowledge_base import views

app_name = 'knowledge_base'


urlpatterns = [
    url(r'^$', views.knowledge_base_list, name='kb_list'),
    url(r'^add/$', views.knowledge_base_add, name='kb_add'),
    url(r'^(?P<statute_chapter>\d+)/(?P<statute_number>\d+)/view/$', views.knowledge_base_statute, name='view_knowledgebase'),
    url(r'^(?P<kb_id>\d+)/view/$', views.knowledge_base_guide, name='view_knowledgebase_guide'),
    url(r'^(?P<type>\w+)/(?P<state>\w+)/(?P<statute_chapter>\d+)/(?P<statute_number>\d+)/api/$', views.statute_as_json, name='view_api'),
    url(r'^(?P<type>\w+)/(?P<state>\w+)/(?P<kb_area>\w+)/(?P<statute_heading>\w+)/api/$', views.element_as_json, name='view_api'),
    url(r'^(?P<type>\w+)/(?P<state>\w+)/api/$', views.all_element_as_json, name='view_api_all'),
]
