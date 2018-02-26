from django.conf.urls import url
from . import views
from . import templates

app_name = 'wechat'
urlpatterns = [
	url(r'^$', views.wechatHome, name='wechatHome'),
	url(r'^addMaterial$', views.addMaterial, name='addMaterial'),
	url(r'^createMenu$', views.createMenu, name='createMenu'),
	url(r'^groupbuyPanel$', views.groupbuyPanel, name='groupbuyPanel'),
	url(r'^takeoutPanel$', views.takeoutPanel, name='takeoutPanel'),
	url(r'^carorderPanel$', views.carorderPanel, name='carorderPanel'),
	url(r'^moviePanel$', views.moviePanel, name='moviePanel'),
]
