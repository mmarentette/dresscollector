from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dresses/', views.dresses_index, name='index'),
    path('dresses/<int:dress_id>/', views.dresses_detail, name='detail')
]