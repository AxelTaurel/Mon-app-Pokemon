from django.contrib import admin
from .models import carte, Attaque

class AttaqueInline(admin.TabularInline):
    model = Attaque
    extra = 1

class CarteAdmin(admin.ModelAdmin):
    inlines = [AttaqueInline]

admin.site.register(carte, CarteAdmin)
