from django.db import models

from datetime import datetime

# Create your models here.

class currency(models.Model):
	currency_from = models.CharField(max_length = 50)
	currency_to = models.CharField(max_length = 50)
        currency_input = models.IntegerField(default=1)
        
        date = models.DateTimeField(default=datetime.now, blank=True)




	def __str__(self):
		return self.currency_to
