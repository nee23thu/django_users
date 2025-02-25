from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=10)
    zip = models.IntegerField(null=True, blank=True)
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
