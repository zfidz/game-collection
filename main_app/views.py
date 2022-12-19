from django.shortcuts import render
from main_app.models import Game
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game

# Create your views here.
from django.http import HttpResponse

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')


# def games_index(request):
#   games = Game.objects.all()
#   return render(request, 'games/index.html', { 'games': games })
class GameList(ListView):
  model = Game
  template_name = 'games/index.html'


class GameCreate(CreateView):
  model = Game
  fields = '__all__'
  success_url = '/games/'

class GameUpdate(UpdateView):
  model = Game
  fields = ['genre', 'description', 'rating']

class GameDelete(DeleteView):
  model = Game
  success_url = '/games/'
  
def games_details(request, game_id):
  game = Game.objects.get(id=game_id)
  return render(request, 'games/details.html', {'game': game})