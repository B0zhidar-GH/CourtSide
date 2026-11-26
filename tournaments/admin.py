from django.contrib import admin
from .models import Tournament, TournamentRegistration

# Register your models here.

class TournamentRegistrationInline(admin.TabularInline):
    model = TournamentRegistration
    extra = 1

@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'location', 'surface', 'status', 'end_date', 'max_players', 'organizer',
                    'status', 'created_at')

    inlines = [TournamentRegistrationInline]

@admin.register(TournamentRegistration)
class TournamentRegistrationAdmin(admin.ModelAdmin):
    list_display = ('tournament', 'player', 'status', 'registered_at',)