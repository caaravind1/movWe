
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('home',views.home),
    path('login',views.log),
    path('admin_home',views.admin_home),
    path('admin_view_theater',views.admin_view_theater),
    path('admin_view_customer',views.admin_view_customer),
    path('admin_manage_type',views.admin_manage_type),
    path('type_delete/<t_id>',views.type_delete),
    path('type_update/<id>',views.type_update),
    path('admin_manage_movie',views.admin_manage_movie),
    path('film_delete/<f_id>',views.film_delete),
    path('film_update/<id>',views.film_update),
    path('admin_manage_timing',views.admin_manage_timing),
    path('timing_delete/<tid>',views.timing_delete),
    path('timing_update/<id>',views.timing_update),
    path('admin_manage_seat',views.admin_manage_seat),
    path('seat_delete/<sid>',views.seat_delete),
    path('seat_update/<id>',views.seat_update),
    path('Theater_reg',views.theater_reg),
    path('theater_home',views.theater_home),
    path('theater_manage_screen',views.theater_manage_screen),
    path('screen_delete/<scid>',views.screen_delete),
    path('screen_update/<id>',views.screen_update),
    path('theater_manage_seating/<id>',views.theater_manage_seating),
    path('seating_delete/<seid>',views.seating_delete),
    path('seating_update/<id>',views.seating_update),
    path('theater_allocate_film',views.theater_allocate_film),
    path('theater_view_booking',views.theater_view_booking),
    path('theater_view_detail/<id>',views.theater_view_detail),
    path('theater_view_customer/<id>',views.theater_view_customer),
        path('theater_view_payment/<id>',views.theater_view_payment),

    path('producer_reg',views.producer_reg),
    path('producer_manage_project',views.producer_manage_project),
    path('prj_delete/<pid>',views.prj_delete),
    path('prj_update/<id>',views.prj_update),
    path('producer_home',views.producer_home),
     path('producer_manage_oppor',views.producer_manage_oppor),
    path('oppor_delete/<oid>',views.oppor_delete),
    path('oppor_update/<id>',views.oppor_update),
    path('producer_add_pref/<id>',views.producer_add_pref),
    path('producer_view_request',views.producer_view_request),


#-------------------------android-----------------------------


    path('api/loginn', views.login),
    path('api/registration', views.registration),
    path('api/chatdetail', views.chatdetail),
    path('api/chat_user', views.chat_user),
    path('api/view_theaters', views.view_theaters),
    path('api/get_movies_for_theater/', views.get_movies_for_theater, name='get_movies_for_theater'),
    path('api/get_opportunities', views.get_opportunities),

    path('api/get_project_details',views.get_project_details),
    path('api/view_seats', views.view_seats),  
    path('api/view_booking', views.view_booking),
    path('api/book_seat', views.book_seat),
    path('api/sendRequest', views.sendRequest),
    path('api/make_payment', views.make_payment),
    path('api/cancel_booking', views.cancel_booking),
    path('api/view_request', views.view_request),
    path('add_images', views.add_images),
    path('api/view_schedule',views. view_schedule),
    path('api/producer_registration',views. producer_registration),
    path('api/get_preferences', views.get_preferences, name='get_preferences'),
        path('api/get_project_details', views.get_project_details),
                path('api/add_community', views.add_community),
                path('api/view_communities', views.view_communities),
                path('api/joincommunity', views.joincommunity),
                
                path('api/joined_comm', views.joined_comm),

    path('manage_project', views.manage_project),
        path('api/view_projects', views.view_projects, name='get_preferences'),
        path('api/delete_project', views.delete_project, name='get_preferences'),
        path('api/add_oppor', views.add_oppor, name='get_preferences'),
                path('api/view_oppor', views.view_oppor, name='get_preferences'),
                path('api/add_pref', views.add_pref, name='get_preferences'),
                    path('api/view_requests', views.view_requests, name='get_preferences'),
                    path('api/add_meeting', views.add_meeting, name='get_preferences'),
                            path('api/get_paid_movies', views.get_paid_movies),

]




    
    
    
