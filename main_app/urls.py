from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dresses/', views.dresses_index, name='index'),
    path('dresses/<int:dress_id>/', views.dresses_detail, name='detail'),
    # Notice that we don't have to put the create view above the detail view because, unlike Express, Django won't match a route unless the second segment has an integer (and therefore it won't match 'create' to the integer above)
    path('dresses/create/', views.DressCreate.as_view(), name='dresses_create'),
    # Note: we must use pk as named parameter instead of dress_id; this is convention for CBVs that work with model instances
    path('dresses/<int:pk>/update/', views.DressUpdate.as_view(), name='dresses_update'),
    path('dresses/<int:pk>/delete/', views.DressDelete.as_view(), name='dresses_delete'),
    path('dresses/<int:dress_id>/add_review/', views.add_review, name='add_review'),
    path('dresses/<int:dress_id>/add_photo/', views.add_photo, name='add_photo'),
    path('dresses/<int:dress_id>/assoc_store/<int:store_id>/', views.assoc_store, name='assoc_store'),
    path('dresses/<int:dress_id>/unassoc_store/<int:store_id>/', views.unassoc_store, name='unassoc_store'),
    path('stores/', views.StoreList.as_view(), name='stores_list'),
    path('stores/<int:pk>/', views.StoreDetail.as_view(), name='stores_detail'),
    path('stores/create/', views.StoreCreate.as_view(), name='stores_create'),
    path('stores/<int:pk>/delete/', views.StoreDelete.as_view(), name='stores_delete'),
    path('stores/<int:pk>/update/', views.StoreUpdate.as_view(), name='stores_update'),
]