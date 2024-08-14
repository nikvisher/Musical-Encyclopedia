from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('peoples/<int:country_id>/', views.peoples, name='peoples'),
    path('instrument_categories/<int:people_id>/', views.instrument_categories, name='instrument_categories'),
    path('instrument_list/<int:category_id>/', views.instrument_list, name='instrument_list'),
    path('instrument_detail/<int:instrument_id>/', views.instrument_detail, name='instrument_detail'),
]

#Каждый маршрут связывает URL-адрес с соответствующим представлением