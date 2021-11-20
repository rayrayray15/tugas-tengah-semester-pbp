from django.db import models

# Create your models here.

class Comment(models.Model):
   name = models.CharField(max_length=255)
   content = models.TextField()
   date = models.DateTimeField(auto_now_add=True)

    #  class Meta:
    #      ordering = ("publish",) 
   def __str__(self):
      return self.name