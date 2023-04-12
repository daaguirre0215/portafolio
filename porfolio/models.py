from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField


class Project(models.Model):
    tittle = CharField(max_length=200)
    description = CharField(max_length=500)
    image = ImageField(upload_to="porfolio/images/")
    url = URLField(blank=True)
