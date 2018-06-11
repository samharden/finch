from django.conf.urls import url
from common import views
from django.contrib.auth import views as auth_views
from django.urls import path


app_name = 'common'

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^login/$', views.login_crm, name="home"),
    url(r'^upload_file/$', views.upload_file, name='upload_files'),
    path('<username>/view/', views.user_profile_page, name='view'),
    path('<username>/edit/', views.edit_user, name='edit'),
]
