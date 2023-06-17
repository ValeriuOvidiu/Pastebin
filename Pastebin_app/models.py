from django.db import models

# Create your models here
class textInput (models.Model):
    textSaved=models.TextField()
    def __str__(self):
        return self.textSaved 
