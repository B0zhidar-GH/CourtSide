from django.urls import path

from matches.views import MatchCreateView

#from tournaments.urls import urlpatterns

urlpatterns = [
    path('tournaments/<int:pk>/matches/create/', MatchCreateView.as_view(), name='match-create')
]