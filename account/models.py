import email
from django.db import models

class CadUser(models.Model):
    nome = models.CharField(max_length=20, null=False)
    email = models.EmailField(null=False)
    senha = models.CharField(max_length=20)

class LogUser(models.Model):
    email = models.EmailField(null=False)
    senha = models.CharField(max_length=20)