from django.db import models
from criminal.models.criminal import Criminal


class Theft(models.Model):
    criminal_id = models.ForeignKey(Criminal, on_delete=models.CASCADE)
    dificulty = models.IntegerField()
    reward = models.IntegerField()

    def __str__(self):
        return f'{self.item_name} ({self.player.username})'
