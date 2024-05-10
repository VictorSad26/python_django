from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="clientes")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to="clientes_photos", null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
