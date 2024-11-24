from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Interface d'administration
    path('', include('pokemon.urls')),  # Inclure les URLs de l'application Pokemon
]

