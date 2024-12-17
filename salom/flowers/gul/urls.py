
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gullar/', views.barcha_gullar, name='barcha_gullar'),
    path('tur/<int:tur_id>/', views.gul_by_tur, name='gul_by_tur'),
    path('gul/<int:gul_id>/', views.gul_detail, name='gul_detail'),
]
