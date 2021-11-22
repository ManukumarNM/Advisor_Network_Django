from django.db import models
from admin_api.models import Advisor
# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=200) 
    user_email = models.EmailField(max_length=200, unique=True)
    user_password = models.CharField(max_length=200)
    advisors = models.ManyToManyField(Advisor)

    def __str__(self):
        return f'User ({self.user_name})'

class Booking(models.Model):
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    def __str__(self):
        return f'Booking ({self.advisor}, {self.user})'