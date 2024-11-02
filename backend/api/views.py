from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import json
from .models import Anime, Character, CharacterAnimeRole
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def handle_anime(request, anime_id=None):
    """Handle CRUD operations for Anime model."""
    if request.method == 'GET':
        if anime_id:
            anime = get_object_or_404(Anime, id=anime_id)
            return JsonResponse({
                'id': anime.id,
                'title': anime.title,
                'description': anime.description,
                'release_date': anime.release_date.isoformat(),
                'is_ongoing': anime.is_ongoing,
                'episodes': anime.episodes,
                'rating': anime.rating
            })
        else:
            animes = Anime.objects.all()
            return JsonResponse({
                'animes': [{
                    'id': anime.id,
                    'title': anime.title,
                    'description': anime.description,
                    'release_date': anime.release_date.isoformat(),
                    'is_ongoing': anime.is_ongoing,
                    'episodes': anime.episodes,
                    'rating': anime.rating
                } for anime in animes]
            })
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        anime = Anime.objects.create(
            title=data['title'],
            description=data['description'],
            release_date=data['release_date'],
            is_ongoing=data['is_ongoing'],
            episodes=data['episodes'],
            rating=data['rating']
        )
        return JsonResponse({'message': 'Created successfully', 'id': anime.id}, status=201)
    
    elif request.method == 'PUT':
        anime = get_object_or_404(Anime, id=anime_id)
        data = json.loads(request.body)
        for key, value in data.items():
            setattr(anime, key, value)
        anime.save()
        return JsonResponse({'message': 'Updated successfully'})
    
    elif request.method == 'DELETE':
        anime = get_object_or_404(Anime, id=anime_id)
        anime.delete()
        return JsonResponse({'message': 'Deleted successfully'})

@csrf_exempt
def handle_character(request, character_id=None):
    """Handle CRUD operations for Character model."""
    if request.method == 'GET':
        if character_id:
            character = get_object_or_404(Character, id=character_id)
            return JsonResponse({
                'id': character.id,
                'name': character.name,
                'description': character.description,
                'birth_date': character.birth_date.isoformat() if character.birth_date else None,
                'age': character.age
            })
        else:
            characters = Character.objects.all()
            return JsonResponse({
                'characters': [{
                    'id': char.id,
                    'name': char.name,
                    'description': char.description,
                    'birth_date': char.birth_date.isoformat() if char.birth_date else None,
                    'age': char.age
                } for char in characters]
            })
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        character = Character.objects.create(
            name=data['name'],
            description=data['description'],
            birth_date=data.get('birth_date'),
            age=data['age']
        )
        return JsonResponse({'message': 'Created successfully', 'id': character.id}, status=201)
    
    elif request.method == 'PUT':
        character = get_object_or_404(Character, id=character_id)
        data = json.loads(request.body)
        for key, value in data.items():
            setattr(character, key, value)
        character.save()
        return JsonResponse({'message': 'Updated successfully'})
    
    elif request.method == 'DELETE':
        character = get_object_or_404(Character, id=character_id)
        character.delete()
        return JsonResponse({'message': 'Deleted successfully'})

@csrf_exempt
def handle_character_role(request, role_id=None):
    """Handle CRUD operations for CharacterAnimeRole model."""
    if request.method == 'GET':
        if role_id:
            role = get_object_or_404(CharacterAnimeRole, id=role_id)
            return JsonResponse({
                'id': role.id,
                'character': {
                    'id': role.character.id,
                    'name': role.character.name
                },
                'anime': {
                    'id': role.anime.id,
                    'title': role.anime.title
                },
                'role': role.role,
                'appearance_episode': role.appearance_episode
            })
        else:
            roles = CharacterAnimeRole.objects.all()
            return JsonResponse({
                'roles': [{
                    'id': role.id,
                    'character': {
                        'id': role.character.id,
                        'name': role.character.name
                    },
                    'anime': {
                        'id': role.anime.id,
                        'title': role.anime.title
                    },
                    'role': role.role,
                    'appearance_episode': role.appearance_episode
                } for role in roles]
            })
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        role = CharacterAnimeRole.objects.create(
            character_id=data['character_id'],
            anime_id=data['anime_id'],
            role=data['role'],
            appearance_episode=data['appearance_episode']
        )
        return JsonResponse({'message': 'Created successfully', 'id': role.id}, status=201)
    
    elif request.method == 'PUT':
        role = get_object_or_404(CharacterAnimeRole, id=role_id)
        data = json.loads(request.body)
        for key, value in data.items():
            setattr(role, key, value)
        role.save()
        return JsonResponse({'message': 'Updated successfully'})
    
    elif request.method == 'DELETE':
        role = get_object_or_404(CharacterAnimeRole, id=role_id)
        role.delete()
        return JsonResponse({'message': 'Deleted successfully'})
