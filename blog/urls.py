from django.conf.urls import url, include
from . import views
from django.conf import settings
import debug_toolbar
from django.urls import path


app_name = 'blog'
urlpatterns = [
    #^$ 시작끝
    #VIEWS.POST_LIST 함수 불러옴
	path(r'^$', views.post_list),
	path(r'^(?P<id>\d+)/$', views.post_detail),


]

if settings.DEBUG :
	urlpatterns += [
	url(r'^__debug__/', include(debug_toolbar.urls)),
	]