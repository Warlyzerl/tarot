from django.db import models

class Card(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=800)

    def __str__(self):
        return self.name