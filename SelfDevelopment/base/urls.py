from django.urls import path
from . import views

urlpatterns = [ path('', views.home, name='home'),
                #path('category/<str:pk>/', views.category, name='category'),
                path('room/<str:pk>/', views.room, name='room'),
                path('create_room/', views.create_room, name='create_room'),
                path('delete_room/<str:pk>/', views.delete_room, name='delete_room'),
                path('update_room/<str:pk>/', views.update_room, name='update_room'),
                path('login/', views.login_page, name='login'),
                path('logout/', views.logout_page, name='logout'),
                path('register/', views.register_page, name='register'),
                path('^prof_page/(?P<username>\w+)/$>/', views.prof_page, name='prof_page'),
]