from django.urls import path

from . import views

urlpatterns = [
	path('', views.main_page, name='main_page'),
    path('park_list/', views.park_list_view, name='state_park_list'),
    path('park_profile/', views.park_profile_view, name='park_profile'),
    path('eco_list/', views.ecoregion_list, name='ecoregion_list'),
    path('eco_profile/', views.eco_profile_view, name='eco_profile_view'),
    path('plant_list/', views.plant_type_list, name='plant_type_list'),
    path('plant_profile/', views.plant_profile_view, name = 'plant_profile_view'),
    path('about/', views.about_page, name='about_page'),
	path('SubPage/',views.sub_page,name='sub_page')
]
