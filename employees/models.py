from django.db import models

from django.utils import timezone


# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    emp_number = models.IntegerField(blank=False, null=False, unique=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    cell_phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.emp_number)