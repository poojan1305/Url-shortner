from django.db import models

# Create your models here.
class Urls(models.Model):
    link= models.CharField(max_length=1000)
    uuid = models.CharField(max_length=100)
    class Meta:
       verbose_name="Urls"
       verbose_name_plural="Urls" 

    def __str__(self):
        return self.link