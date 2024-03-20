from django.db import models
from django.contrib.auth.models import User


class Diaries(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    memo = models.TextField()
    tags = models.TextField()

    class Meta:
        managed = False
        db_table = "Diaries"
