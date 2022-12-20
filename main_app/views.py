from django.shortcuts import render, redirect
from main_app.models import Game
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game
from .forms import SessionForm
# Create your views here.
from django.http import HttpResponse

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def games_details(request, game_id):
  game = Game.objects.get(id=game_id)
  session_form = SessionForm()
  return render(request, 'games/details.html', {'game': game, 'session_form' : session_form})

def add_session(request, game_id):
    # create a ModelForm instance using the data in request.POST
  form = SessionForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_session = form.save(commit=False)
    new_session.game_id = game_id
    new_session.save()
  return redirect('detail', game_id=game_id)

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