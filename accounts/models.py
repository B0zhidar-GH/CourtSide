from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Create your models here.

class Account(AbstractUser):
    pass

class PlayerProfile(models.Model):

    class PlayingHand(models.TextChoices):
        RIGHT = 'right', 'Right-handed'
        LEFT = 'left', 'Left-handed'

    class FavouriteSurface(models.TextChoices):
        HARD = 'hard', 'Hard court'
        CLAY = 'clay', 'Clay court'
        GRASS = 'grass', 'Grass court'
        INDOOR_HARD = 'indoor hard', 'Indoor Hard court'

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')

    country = models.CharField(max_length=30, blank=True)
    bio = models.TextField(max_length=300, blank=True)
    playing_hand = models.CharField(max_length=15, choices=PlayingHand.choices, blank=True)
    favourite_court_surface = models.CharField(max_length=15, choices=FavouriteSurface.choices, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    favourite_player = models.CharField(max_length=30, blank=True)
    racket = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s profile"