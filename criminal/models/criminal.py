from django.db import models


class Criminal(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    money = models.IntegerField(default=0)
    crime_points = models.IntegerField(default=0)
    criminal_classification_id = models.ForeignKey('Classification', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


