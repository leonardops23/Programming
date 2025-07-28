from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('hechos/', views.FactListView.as_view(), name='fact_list'),
    path('hecho/<int:pk>/', views.FactDetailView.as_view(), name='fact_detail'),
    path('categoria/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('buscar/', views.SearchView.as_view(), name='search'),
]