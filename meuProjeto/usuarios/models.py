from django.contrib.auth.models import User
from django.db import models


class Cliente(User):
    age = models.PositiveIntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to="clientes_photos", null=True, blank=True)
