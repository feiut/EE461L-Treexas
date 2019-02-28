from django.urls import path

from . import views

urlpatterns = [
	path('', views.page_1, name='page_1'),

    path('park_list/', views.state_park_list, name='state_park_list'),
    path('park1/', views.pedernales_park, name='pedernales'),
    path('park2/', views.dinosaur_valley_park, name='dinosaur_valley'),
    path('park3/', views.daingerfield_park, name='daingerfield'),
    path('park4/', views.acton_park, name='acton'),
    path('eco_list/', views.ecoregion_list, name='ecoregion_list'),
    path('eco1/', views.piney_eco, name='piney'),
    path('eco2/', views.marshes_eco, name='marches'),
    path('eco3/', views.postoaksavanah_eco, name='postoak'),
    path('plant_list/', views.plant_type_list, name='plant_type_list'),
    path('plant_profile/', views.plant_profile_view, name = 'plant_profile_view'),
    path('about/', views.about_page, name='about_page')
]
