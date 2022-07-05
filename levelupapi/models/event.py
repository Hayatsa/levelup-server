from django.db import models
from levelupapi.models.game import Game
from levelupapi.models.gamer import Gamer


class Event(models.Model):

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    description = models.TextField(max_length=200)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    organizer = models.ForeignKey(Gamer, on_delete=models.CASCADE)