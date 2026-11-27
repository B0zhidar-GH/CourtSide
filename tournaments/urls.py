#from django import views
from django.urls import path
from . import views

#from courtside.urls import urlpatterns
from .views import (HomeView, TournamentListView, TournamentDetailView,
                    TournamentCreateView, TournamentUpdateView,
                    TournamentDeleteView, TournamentRegisterView, TournamentRegistrationView, manage_registration)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('tournaments/', TournamentListView.as_view(), name='tournament-list'),
    path('tournaments/<int:pk>/', TournamentDetailView.as_view(), name='tournament-detail'),
    path('tournaments/create/', TournamentCreateView.as_view(), name='tournament-create'),
    path('tournaments/<int:pk>/eidt/', TournamentUpdateView.as_view(), name='tournament-edit'),
    path('tournaments/<int:pk>/delete/', TournamentDeleteView.as_view(), name='tournament-delete'),
    path('tournaments/<int:pk>/register/', TournamentRegisterView.as_view(), name='tournament-register'),
    path('tournaments/<int:pk>/registrations/', TournamentRegistrationView.as_view(),
         name='tournament-registrations'),
    path('tournaments/<int:pk>/registrations/<int:registration_pk>/manage/', views.manage_registration,
         name='manage-registration')

]
