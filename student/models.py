from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    std = models.IntegerField(default=1)

    def __str__(self):
        return self.name

