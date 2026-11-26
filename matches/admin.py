from django.contrib import admin
from .models import  Match, MatchSet

# Register your models here.

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('tournament', 'player1', 'player2', 'winner', 'round_number', 'scheduled_at', 'status',
                    'created_at')

@admin.register(MatchSet)
class MatchSetAdmin(admin.ModelAdmin):
    list_display = ('match', 'set_number', 'player1_games', 'player2_games',)