from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserInfoProfile(models.Model):
    # create the user and connect is one to connect
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional optional class
    user_portfolio_site = models.URLField(blank=True)
    user_dp = models.ImageField(upload_to='display_p', blank=True)

    def __str__(self):
        # for this class to return the username of the user
        return self.user.username
