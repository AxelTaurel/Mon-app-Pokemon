from django.urls import path
from . import views

urlpatterns = [
    path('cartes/', views.collection_list, name='collection_list'),  # Liste des cartes
    path('carte/<int:pk>/detail/', views.carte_detail, name='carte_detail'),  # Détails d'une carte
    path('carte/<int:pk>/modifier/', views.modifier_pv, name='modifier_pv'),  # Modifier les PV
    path('', views.collection_list, name='home'),  # Page d'accueil
]
