from django.db import models

class Crime(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.IntegerField()
    reward = models.IntegerField()

    def __str__(self):
        return self.name
