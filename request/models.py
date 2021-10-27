from datetime import datetime

from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


class Request(models.Model):
    Category = (
        ('Appliance', 'Appliance'),
        ('Carpentry', 'Carpentry'),
        ('Club House', 'Club House'),
        ('Common Area','Common Area'),
        ('Door Codes','Door Codes'),
        ('Doors/Windows','Doors/Windows'),
        ('Electrical','Electrical'),
        ('Flooring/Carpenting','Flooring/Carpenting'),
        ('Grounds','Grounds'),
        ('Laundry Rooms','Laundry Rooms'),
        ('Other','Other')


    )
    request_type = (
        ('New', 'New'),
        ('In-progress', 'In-progress'),
        ('Completed', 'Completed')
    )
    # nuid = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, )
    username = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, )
    Location = (
        ('Kitchen', 'Kitchen'),
        ('Bathroom', 'Bathroom'),
        ('Master Bathroom', 'Master Bathroom'),
        ('Master Bedroom', 'Master Bedroom'),
        ('Hallway', 'Hallway'),
        ('Patio', 'Patio'),
        ('Second Bedroom', 'Second Bedroom'),
        ('Foyer', 'Foyer'),
        ('Balcony', 'Balcony')


    )
    request_date = models.DateField(default=datetime.now())
    full_description= models.TextField()
    category_type = models.CharField(max_length=40,
                           choices=Category,
                           default='')
    status = models.CharField(max_length=20,
                              choices=request_type,
                              default='New')
    location_type = models.CharField(max_length=40,
                              choices=Location,
                              default='')

    def __str__(self):
        return f"{self.username} - {self.status} - {self.request_date}"






