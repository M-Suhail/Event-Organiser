from django.urls import path, re_path
from . import views

app_name = 'events'

urlpatterns = [
    path('search-event/', views.search_event, name='search_event'),
    path('', views.events_list, name='events_list'),
    path('archived_list/', views.archived_list, name='archived_list'),
    path('add_event/', views.add_event, name='add_event'),
    path('archive_event/<int:id>/', views.archive_event, name='archive_event'),
    path('edit_event/<int:id>/', views.edit_event, name='edit_event'),
    path('<slug:slug>', views.delete_event, name='delete_event'),
    path('details/<int:id>/', views.event_details, name='event_details'),

]
