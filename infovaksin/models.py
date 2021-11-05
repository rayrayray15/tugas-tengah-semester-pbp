from django.db import models

# Create your models here.

class Comment(models.Model):
     name = models.CharField(max_length=50)
     content = models.TextField()
     publish = models.DateTimeField(auto_now_add=True)

    #  class Meta:
    #      ordering = ("publish",) 
     def __str__(self):
        return f"Comment by {self.name}"