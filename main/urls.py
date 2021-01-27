from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('egazat', views.egazat),
    path('quran', views.quran),
    path('tajweed', views.tajweed),
    path('about', views.about),
    path('quran/register_q', views.register_q, name='form'),
    path('tajweed/register_t', views.register_t),
    path('egazat/register_e', views.register_e),
]
