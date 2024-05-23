from venv import create
from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=200)
    update_at = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)
    
    
class Item (models.Model):
    update_at = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)
    todo = models.ForeignKey(Todo, on_delete= models.CASCADE, related_name= 'items')
    text =  models.TextField(max_length=100)
    complete  = models.BooleanField(default=False)
    