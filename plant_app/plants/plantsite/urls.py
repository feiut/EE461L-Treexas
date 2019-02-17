from django.urls import path

from . import views

urlpatterns = [
	path('', views.page_1, name='page_1'),

    path('park_list/', views.state_park_list, name='state_park_list'),
    path('park1/', views.pedernales_park, name='pedernales'),
    path('park2/', views.dinosaur_valley_park, name='dinosaur_valley'),
    path('park3/', views.daingerfield_park, name='daingerfield'),
    path('park4/', views.acton_park, name='acton'),
]