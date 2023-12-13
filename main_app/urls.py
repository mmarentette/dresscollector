from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dresses/', views.dresses_index, name='index'),
    path('dresses/<int:dress_id>/', views.dresses_detail, name='detail'),
    # Notice that we don't have to put the create view above the detail view because, unlike Express, Django won't match a route unless the second segment has an integer (and therefore it won't match 'create' to the integer above)
    path('dresses/create/', views.DressCreate.as_view(), name='dresses_create'),
]