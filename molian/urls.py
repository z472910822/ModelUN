from django.urls import path
from . import views
from django.conf.urls import url, include
from django.conf import settings

app_name = 'learning_logs'

urlpatterns = [
	path('post_new/', views.post_new, name='post_new'),
    path('base/',views.base,name='base'),
    path('post_list/',views.post_list,name='post_list'),
    path('testapi/',views.getAllArticles,name="testapi"),
]
