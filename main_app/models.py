from django.db import models
from django.urls import reverse

RATING_CHOICES = (
  ('E', 'E'),
  ('T','T'),
  ('M','M')
)

# Create your models here.

class Character(models.Model):
  name = models.CharField(max_length=25)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('characters_detail', kwargs={'pk': self.id})

class Game(models.Model):
  name = models.CharField(max_length=25)
  rating = models.CharField(max_length=25, choices=RATING_CHOICES, default='E')
  genre = models.CharField(max_length=25)
  description = models.TextField(max_length=250)

  def __str__(self):
    return f'{self.name} ({self.id})'  

  def get_absolute_url(self):
    return reverse('detail',kwargs={'game_id': self.id})
    # return /games/{self.id}

class Session(models.Model):
  length = models.CharField(max_length=20)
  date = models.DateField('Date Played')
  game=models.ForeignKey(Game, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.length} on {self.date}"

  class Meta:
    ordering = ['-date']  