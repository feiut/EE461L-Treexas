from django.urls import path

from . import views

urlpatterns = [
	path('', views.page_1, name='page_1'),
    path('page_2/', views.page_2, name='page_2'),
    path('page_3/', views.page_3, name='page_3'),
    path('page_4/', views.page_4, name='page_4'),
    path('page_5/', views.page_5, name='page_5'),
    path('page_6/', views.page_6, name='page_6')
	]