from django.conf.urls import url
from . import views
from . import templates

app_name = 'wechat'
urlpatterns = [
	url(r'^$', views.wechatHome, name='wechatHome'),
	url(r'^addMaterial$', views.addMaterial, name='addMaterial'),
	url(r'^createMenu$', views.createMenu, name='createMenu'),
	url(r'^takeawayPanel$', views.takeawayPanel, name='takeawayPanel'),
	url(r'^moviePanel$', views.moviePanel, name='moviePanel'),
	url(r'^groupbuyPanel$', views.groupbuyPanel, name='groupbuyPanel'),
	url(r'^carorderPanel$', views.carorderPanel, name='carorderPanel'),
	url(r'^shoppingPanel$', views.shoppingPanel, name='shoppingPanel'),
]
