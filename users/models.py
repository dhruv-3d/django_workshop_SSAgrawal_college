from django.db import models
from django.contrib.auth.models import User


ROLE_CHOICES = (
    (1, 'Student'),
    (2, 'Faculty')
)

GENDER_CHOICES = (
    ('F', 'Female'),
    ('M', 'Male')
)

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    role = models.IntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='users/media/profile')

    def __str__(self):
        return self.user.username

