from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^upload/$',views.new_project,name='add_project'),
    url(r'^review/(?P<project_id>\d+)', views.review_project, name='review'),
    url(r'^searched/', views.search_projects, name='search'),




]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
