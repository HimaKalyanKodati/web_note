from django.db import models

# Create your models here.
class Note(models.Model):
    
    # def __str__(self) -> str:
    #     return self.id
    
    content=models.CharField(max_length=500)