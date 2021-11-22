from django.db import models

# Create your models here.
class Advisor(models.Model):
    advisor_name = models.CharField(max_length=200)
    photo_url = models.URLField(max_length=500)

    def __str__(self):
        return f"Advisor({self.advisor_name}, {self.photo_url})"

        
