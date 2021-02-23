from django.urls import path
from . import views


urlpatterns = [
    path('ballina/', views.home, name='Joy-home'),
    path('ballina1/', views.home1, name='Joy-home1'),
    path('per_ne/', views.about, name='Joy-about'),
    path('kontakti/', views.createpost, name='Joy-contact'),
    path('kinemaja/', views.cinema, name='Joy-cinema'),
    path('kursi/', views.course, name='Joy-course'),
    path('kursi1/', views.course1, name='Joy-course1'),
    path('kursi2/', views.course2, name='Joy-course2'),
    path('kursi3/', views.course3, name='Joy-course3'),
    path('kursi4/', views.course4, name='Joy-course4'),
    # path('kyqu/', views.log, name='Joy-log'),
    path('eventet/', views.chance, name='Joy-events'),
   # path('regjistrohu/', views.register, name='Joy-register'),
]