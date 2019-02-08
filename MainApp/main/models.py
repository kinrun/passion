from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
# Adding columns to default Django User Model
class Profile(models.Model):
    # link to default django User Model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #gender = models.CharField(max_length=10, blank=True)
    #bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    balance_btc = models.CharField(max_length=30, blank=True)
    balance_eth = models.CharField(max_length=30, blank=True)
    address_btc = models.CharField(max_length=30, blank=True)
    address_eth = models.CharField(max_length=30, blank=True)
    #birth_date = models.DateField(null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()