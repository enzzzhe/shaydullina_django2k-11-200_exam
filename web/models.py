from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)
    answer = models.CharField(max_length=3)

    def __str__(self):
        return self.text