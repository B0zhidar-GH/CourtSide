from django.contrib import admin
from .models import Account, PlayerProfile

# Register your models here.

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')

@admin.register(PlayerProfile)
class PlayerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'country', 'bio', 'playing_hand', 'favourite_court_surface', 'age', 'height',
                    'favourite_player', 'racket', 'created_at')