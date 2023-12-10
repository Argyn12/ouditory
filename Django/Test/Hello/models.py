from django.db import models

# Create your models here.
# myapp/modls.py

from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    descripton = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name