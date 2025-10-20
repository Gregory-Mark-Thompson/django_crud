from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('armies/', views.army_index, name='army-index'),
    path('armies/<int:army_id>/', views.army_detail, name='army-detail'),
    path('armies/create/', views.ArmyCreate.as_view(), name='army-create'),
    path('armies/<int:pk>/update/', views.ArmyUpdate.as_view(), name='army-update'),
    path('armies/<int:pk>/delete/', views.ArmyDelete.as_view(), name='army-delete'),
    path(
        'armies/<int:army_id>/add-battle/',
        views.add_battle,
        name='add-battle'
    ),
    path('accounts/signup/', views.signup, name='signup'),
    path('armies/<int:army_id>/battles/<int:battle_id>/update/', views.BattleUpdate.as_view(), name='battle-update'),
    path('armies/<int:army_id>/battles/<int:battle_id>/delete/', views.BattleDelete.as_view(), name='battle-delete'),
]