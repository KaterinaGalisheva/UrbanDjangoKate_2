from django.db import models

# Create your models here.
# каждый класс это таблица

class Buyer(models.Model):
    name = models.CharField(max_length=15)
    balance = models.DecimalField(decimal_places=2, max_digits=15, blank=True, null=True)
    age = models.IntegerField()


class Game(models.Model):
    title = models.CharField(max_length=30)
    cost = models.DecimalField(decimal_places=2 , max_digits=15)
    size = models.DecimalField(decimal_places=2 , max_digits=15)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')


