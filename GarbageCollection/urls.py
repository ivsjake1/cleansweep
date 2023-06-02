from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('CollectionSchedule/', views.collection, name='collection'),
    path('News/', views.news, name='news'),
    path('News/<int:id>', views.news_detail, name="news_detail"),
    path('RequestPickup/', views.pickup, name='pickup'),
    path('RequestPickupDetail/<int:id>/', views.pickup_details, name='pickup_details'),
    path('PickupListP/', views.pickup_list, name='pickup_list'),
    path('Me', views.profile, name='profile'),
    path('Me', views.add_address, name='add_address'),
    path('Me', views.edit_address, name='edit_address'),
    path('update_password', views.update_password, name='update_password'),
    path('PickupListC/', views.pickup_list_complete, name='pickup_list_complete'),
    path('PickupListO/', views.pickup_list_ontheway, name='pickup_list_ontheway'),
    path('delete-request/<int:id>/', views.delete_request, name='delete-request'),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),


]
