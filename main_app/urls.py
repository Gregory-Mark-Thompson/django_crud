from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('armies/', views.army_index, name='army-index'),
    path('armies/<int:army_id>/', views.army_detail, name='army-detail')
]