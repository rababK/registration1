from django.db import models
from django.contrib.auth.models import AbstractUser

gender_choices=[('female','female'),('male','male')]
class User(AbstractUser):
  gender = models.CharField(choices=gender_choices,max_length =7, blank = True)
  email = models.EmailField( unique = True)
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username','gender']
  def __str__(self):
      return "{}".format(self.email)