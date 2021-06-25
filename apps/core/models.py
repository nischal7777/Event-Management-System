from django.db import models

# Create your models here.


class Reservation(models.Model):
    class Meta:
        db_table = "reservation"
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(null=False, blank=False, unique=False)
    phone = models.CharField(max_length=255, null=False, blank=False)
    date = models.DateField(null=False, blank=False)

    def __str__(self) -> str:
        return self.name
