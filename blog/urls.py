from django.conf.urls import url
from . import views

urlpatterns = [
    #^$ 시작끝
    #VIEWS.POST_LIST 함수 불러옴
	url(r'^$', views.post_list)
]