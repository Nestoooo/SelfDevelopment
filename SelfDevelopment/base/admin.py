from django.contrib import admin
from .models import Category, Room, Message

# Register my models to the admin panal.
admin.site.register(Category)
admin.site.register(Room)
admin.site.register(Message)
