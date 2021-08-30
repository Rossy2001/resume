from django.db import models

# Create your models here.
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    subject=models.CharField(max_length=150,default='')
    message=models.TextField(max_length=150)
    def __str__(self):
        return self.name