from django.db import models
from django.contrib.auth.models import User

# tables in my database to save the entered data in it


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Room (models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    room = models.CharField(max_length=200)
    description = models.TextField(max_length=400, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    #participants
    
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.room
    
class Message (models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    room= models.ForeignKey(Room, on_delete=models.CASCADE)
    body= models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body



