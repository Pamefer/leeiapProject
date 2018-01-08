# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Reconocimiento(models.Model):
    id = models.AutoField(primary_key=True)
    user_logeado=models.ForeignKey(User, related_name='reconocimiento_logeado', blank=True, null=True)
    user_reconocido=models.ForeignKey(User, related_name='reconocimiento_reconocido', blank=True, null=True)
    nombreFoto = models.CharField(max_length=50, blank=True, null=True)
    fechaHora=models.DateTimeField(blank=True, null=True)
    confidence=models.DecimalField( max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Reconocimiento'


class NumReconocimiento(models.Model):
    num_reconocimientos=models.IntegerField(default=1)
