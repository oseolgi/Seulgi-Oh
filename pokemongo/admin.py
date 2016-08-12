from django.contrib import admin

from pokemongo.models import Trainer, Pokemon, Capture

class AdminTrainer (admin.ModelAdmin):
    list_display = ("trainer_id", "trainer_name", "trainer_regdate")
    list_filter = ("trainer_id", "trainer_name", "trainer_regdate")

class AdminPokemon (admin.ModelAdmin):
    list_display = ("pokemon_name", "pokemon_type")
    list_filter = ("pokemon_name", "pokemon_type")

class AdminCapture (admin.ModelAdmin):
    list_display = ("trainer", "pokemon", "pokemon_type", "location", "date")
    list_filter = ("trainer", "pokemon", "location", "date")

    def pokemon_type(self, capture):
        return capture.pokemon.pokemon_type

admin.site.register(Trainer, AdminTrainer)
admin.site.register(Pokemon, AdminPokemon)
admin.site.register(Capture, AdminCapture)
