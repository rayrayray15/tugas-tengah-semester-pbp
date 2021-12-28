from django.db import models

class Feedback(models.Model):
    comments = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
