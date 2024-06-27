from django.db import models

#create
class Category(models.Model):
    name=models.Charfield(max_length=20)