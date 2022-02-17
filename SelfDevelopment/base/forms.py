from django.forms import ModelForm
from .models import Room, Message

#room model to use it when creating or updating a room
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host']

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'