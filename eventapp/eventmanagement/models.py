from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class EventRegistration(models.Model):
    EVENT_CHOICES = [
        ('marriage', 'Marriage'),
        ('birthday', 'Birthday'),
        ('baby_shower', 'Baby Shower'),
        ('anniversary', 'Anniversary'),
        ('housewarming', 'Housewarming'),
        ('graduation', 'Graduation'),
        ('engagement', 'Engagement'),
        ('religious', 'Religious Ceremony'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    occupation = models.CharField(max_length=100)
    event_type = models.CharField(max_length=20, choices=EVENT_CHOICES)
    comments = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.event_type}"
