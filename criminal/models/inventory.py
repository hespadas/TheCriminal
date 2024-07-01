from django.db import models

from .criminal import Criminal

class Inventory(models.Model):
    criminal_id = models.ForeignKey(Criminal, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.item_name} ({self.player.username})'
