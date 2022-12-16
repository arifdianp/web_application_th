from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    mitigation_strategy = models.TextField()
    last_updated_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + '|' + self.description

    def get_absolute_url(self):
        return reverse('home')

#another
