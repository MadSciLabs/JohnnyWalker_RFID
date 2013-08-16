from django.db import models

class Drink(models.Model):
    rfid = models.CharField(max_length=20)
    type = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField()

    def __unicode__(self):
        return self.rfid

# Create your models here.
