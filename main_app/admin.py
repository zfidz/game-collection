from django.contrib import admin
from .models import Game, Session, Character

# Register your models here
admin.site.register(Game)
admin.site.register(Session)
admin.site.register(Character)