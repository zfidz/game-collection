from django.shortcuts import render
from main_app.models import Game


# Create your views here.
from django.http import HttpResponse

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def games_index(request):
  games = Game.objects.all()
  return render(request, 'games/index.html', { 'games': games })

def games_details(request, game_id):
  game = Game.objects.get(id=game_id)
  return render(request, 'games/details.html', {'game': game})