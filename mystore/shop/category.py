from django.db import models

#create
class Category(models.Model):
    name=models.CharField(max_length=20)