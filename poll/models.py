from django.db import models
from django.contrib.auth.models import User

default_creator_id = 1

class Poll(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=default_creator_id)
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count
