import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Portfolio(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length = 30)
    ordering = models.CommaSeparatedIntegerField(max_length = 250, blank=True)

    class Meta:
    	ordering = ['name']

    class Admin:
        pass

    def __unicode__(self):
        return self.name

class Position(models.Model):
    portfolio = models.ForeignKey(Portfolio,
		edit_inline=models.TABULAR, num_in_admin=10)

    POSITION_CHOICES = ( ('L', 'Long'), ('S', 'Short'), )
    position = models.CharField(max_length=1, choices=POSITION_CHOICES,
				default=None, blank=True, null=True)
    symbol = models.CharField(max_length=6, core=True)
    shares = models.PositiveIntegerField(blank=True, null=True)
    open_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    open_date = models.DateField(blank=True, null=True)
    close_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    close_date = models.DateField(blank=True, null=True)

    class Admin:
        pass

    def __unicode__(self):
        return self.symbol
