from django.db import models

# Create your models here.


class school(models.Model):
    ScName= models.CharField(max_length=100, primary_key=True)
    ScPrincipal= models.CharField(max_length=100)
    ScLoc= models.CharField(max_length=100)
    ScId= models.IntegerField()

    def __str__(self):
        return self.ScPrincipal


class student(models.Model):
    ScName= models.ForeignKey(school, on_delete= models.CASCADE)
    Sname= models.CharField(max_length=100)
    ClassName= models.CharField(max_length=100)
    Sid= models.IntegerField(primary_key=True)

    def __str__(self):
        return self.Sname