from django.db import models

RATING_CHOICES = (
  ('E', 'E'),
  ('T','T'),
  ('M','M')
)

# Create your models here.
class Game(models.Model):
  name = models.CharField(max_length=25)
  rating = models.CharField(max_length=25, choices=RATING_CHOICES, default='E')
  genre = models.CharField(max_length=25)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name