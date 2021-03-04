from django.urls import path
from users import views as views1
from . import views

urlpatterns = [

    path('', views.home, name='event-home'),
    path('event_view/', views.event_view, name='event-view'),
    path('about/', views.about, name='event-about'),
    path('register/', views1.register, name='users-register'),

    # CRUD operation on Event
    path('event_view/add/', views.event_add, name='event_add'),
    path('event_view/<int:my_id>/update',
         views.event_update, name='event_update'),
    path('event_view/<int:my_id>/updated',
         views.event_updated, name='event_updated'),

    path('event_view/<int:my_id>/delete',
         views.event_delete, name='event_delete'),
    path('event_details/<int:my_id>', views.event_details, name='event_details'),
    path('user_Details/<slug:username>',
         views.user_details, name='user_details'),

    # Event Booking
    path('booked/<int:e_id>', views.book_request, name='booking'),
    path('event_user/<int:event_id>',
         views.event_user, name='event_user'),

    path('event_user/<int:event_id>/<int:user_id>/conformed',
         views.event_user_conformation, name='event_user_conformation'),

    path('event_user/<int:event_id>/<int:user_id>/unbooked',
         views.event_user_unbooked, name='event_user_unbooked'),

    path('event_user/<int:event_id>/<int:user_id>/attended',
         views.event_user_attended, name='event_user_attended'),

    path('event_user/<int:event_id>/<int:user_id>/certified',
         views.event_user_certified, name='event_user_certified'),

    # Mybooking
    path('my_event/', views.my_event, name='my_event'),
    path('my_event/Requested', views.my_event_requested, name='my_event_requested'),
    path('my_event/Conformed', views.my_event_conformed, name='my_event_conformed'),
    path('my_event/Attended', views.my_event_attended, name='my_event_attended'),





]
