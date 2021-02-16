from django.urls import path

from . import views

urlpatterns = [
	path('', views.homepage, name='homepage'),
	path('scheme/', views.scheme, name='scheme'),
	path('sign_up/', views.sign_up_view, name='sign_up'),
]
