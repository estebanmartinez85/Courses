from django.db import models

# Create your models here.


class Library(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title


