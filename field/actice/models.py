from django.db import models
import pytz
# Create your models here.
class Actice(models.Model):
    id= models.BigAutoField(primary_key=True)
    datetime= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.datetime
    class Meta:
        db_table='actice'
class aaa(models.Model):
    name =models.CharField(max_length=50)
    email = models.EmailField()
class bbb(models.Model):
    tile=models.CharField(max_length=50)
    con=models.TextField()
    aa = models.ForeignKey("aaa",on_delete=models.CASCADE)