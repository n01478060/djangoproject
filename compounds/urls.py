from django.urls import path
from . import views

urlpatterns = [
    path('', views.compounds_list, name='compounds_list'),
    path('compound/<int:pk>/', views.compound_detail, name='compound_detail'),
    path('computed_mw/', views.computed_mw, name='computed_mw'),
    path('computed_mw/new/', views.computed_mw_new, name='computed_mw_new'),
    path('compound_data/<int:pk>/', views.compound_data, name='compound_data'),
]
