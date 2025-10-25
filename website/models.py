from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Portfolio(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    amount = models.FloatField()
