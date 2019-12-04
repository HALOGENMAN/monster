from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=1100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name