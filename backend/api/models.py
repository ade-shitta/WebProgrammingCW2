from django.db import models

# Create your models here.

class Anime(models.Model):
    """Model representing an anime series."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    is_ongoing = models.BooleanField(default=True)
    episodes = models.IntegerField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    
    def __str__(self):
        return self.title

class Character(models.Model):
    """Model representing an anime character."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    birth_date = models.DateField(null=True, blank=True)
    age = models.IntegerField()
    animes = models.ManyToManyField(Anime, through='CharacterAnimeRole')
    
    def __str__(self):
        return self.name

class CharacterAnimeRole(models.Model):
    """Through model representing a character's role in an anime."""
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    role_choices = [
        ('MC', 'Main Character'),
        ('SC', 'Supporting Character'),
        ('ANT', 'Antagonist'),
        ('GC', 'Guest Character')
    ]
    role = models.CharField(max_length=3, choices=role_choices)
    appearance_episode = models.IntegerField()
    
    def __str__(self):
        return f"{self.character.name} in {self.anime.title} as {self.get_role_display()}"
