from django.db import models
from django.db.models.fields import CharField, DateField, TextField
from django.db.models.fields.files import ImageField
import datetime


class Post(models.Model):
    tittle = CharField(max_length=500)
    descripcion = TextField()
    imagen = ImageField(upload_to="blog/images")
    date = DateField(datetime.date.today)
