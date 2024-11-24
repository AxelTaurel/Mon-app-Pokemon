from django.shortcuts import render, get_object_or_404, redirect
from .models import carte
from .forms import cartePvForm

# Vue pour afficher la liste des cartes
def collection_list(request):
    cartes = carte.objects.all()  # Récupère toutes les cartes
    return render(request, 'pokemon/collection_list.html', {'cartes': cartes})

# Vue pour afficher les détails d'une carte

def carte_detail(request, pk):
    carte_instance = get_object_or_404(carte, pk=pk)
    attaques = carte_instance.attaques.all()  # Récupère toutes les attaques liées à la carte
    return render(request, 'pokemon/carte_detail.html', {'carte': carte_instance, 'attaques': attaques})


# Vue pour modifier les PV d'une carte
def modifier_pv(request, pk):
    carte_instance = get_object_or_404(carte, pk=pk)  
    if request.method == 'POST':
        form = cartePvForm(request.POST, instance=carte_instance)
        if form.is_valid():
            form.save()  # Sauvegarde les modifications
            return redirect('collection_list')  # Redirige vers la liste des cartes
    else:
        form = cartePvForm(instance=carte_instance)
    return render(request, 'pokemon/modifier_pv.html', {'form': form, 'carte': carte_instance})
