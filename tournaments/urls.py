from django.urls import path

#from courtside.urls import urlpatterns
from .views import (HomeView, TournamentListView, TournamentDetailView,
                    TournamentCreateView, TournamentUpdateView,
                    TournamentDeleteView, TournamentRegisterView)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('tournaments/', TournamentListView.as_view(), name='tournament-list'),
    path('tournaments/<int:pk>/', TournamentDetailView.as_view(), name='tournament-detail'),
    path('tournaments/create/', TournamentCreateView.as_view(), name='tournament-create'),
    path('tournaments/<int:pk>/eidt/', TournamentUpdateView.as_view(), name='tournament-edit'),
    path('tournaments/<int:pk>/delete/', TournamentDeleteView.as_view(), name='tournament-delete'),
    path('tournaments/<int:pk>/register/', TournamentRegisterView.as_view(), name='tournament-register')
]
