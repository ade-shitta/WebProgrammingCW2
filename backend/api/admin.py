from django.contrib import admin
from .models import Anime, Character, CharacterAnimeRole

# Register your models here.
admin.site.register(Anime)
admin.site.register(Character)
admin.site.register(CharacterAnimeRole)
