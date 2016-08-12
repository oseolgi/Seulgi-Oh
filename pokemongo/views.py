from django.shortcuts import render
from pokemongo.models import Pokemon

def pokemon_list(request):
    qs = Pokemon.objects.all()
    return render(request, 'pokemongo/pokemon_list.html', {
        'pokemon_list': qs,
        })
