from django.conf import settings
from django.db import models
from django.db.models import Q

from matches.models import Match
from tournaments.models import Tournament


class Comment(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")

    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=True, blank=True, related_name="comments",)

    match = models.ForeignKey(Match, on_delete=models.CASCADE, null=True, blank=True, related_name="comments",)

    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

        constraints = [models.CheckConstraint(condition=(Q(tournament__isnull=False, match__isnull=True)
                    | Q(tournament__isnull=True, match__isnull=False)),name="comment_has_exactly_one_target")]

    def __str__(self):
        return f"Comment by {self.author}"