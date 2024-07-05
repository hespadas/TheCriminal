from django.db import models
from django.contrib.auth.models import User


class Criminal(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    money = models.IntegerField(default=0)
    crime_points = models.IntegerField(default=0)
    criminal_classification_id = models.ForeignKey('Classification', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='')
    created_at = models.DateTimeField(auto_now_add=True)
    stamina = models.IntegerField(default=100)

    def __str__(self):
        return self.name

