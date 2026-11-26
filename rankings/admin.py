from django.contrib import admin
from .models import RankingSeason, RankingEntry

# Register your models here.

class RankingEntryInline(admin.TabularInline):
    model = RankingEntry
    extra = 1


@admin.register(RankingSeason)
class RankingSeasonAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
    inlines = [RankingEntryInline]


@admin.register(RankingEntry)
class RankingEntryAdmin(admin.ModelAdmin):
    list_display = (
        'season',
        'player',
        'points',
        'matches_played',
        'wins',
    )