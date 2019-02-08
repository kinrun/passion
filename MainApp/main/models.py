from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.
# Adding columns to default Django User Model
class Profile(models.Model):
    # link to default django User Model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #gender = models.CharField(max_length=10, blank=True)
    #bio = models.TextField(max_length=500, blank=True)
    country = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    balance_btc = models.CharField(max_length=30, blank=True, default='0')
    balance_eth = models.CharField(max_length=30, blank=True, default='0')
    address_btc = models.CharField(max_length=30, blank=True)
    address_eth = models.CharField(max_length=30, blank=True)
    #birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

SERVICE_CHOICES = (
        ('massage', 'Massage'),
        ('sex', 'Sex'),
        ('escort', 'Escort')
    )

PAY_CHOICES = (
        ('b', 'BTC'),
        ('e', 'ETH'),
    )

PLACE_CHOICES = (
        ('h', 'Hotel'),
        ('s', 'Sauna'),
        ('a', 'Appartaments'),
        ('g', "Girl's place"),
    )

STATUS_CHOICES = (
        ('a', 'Requested by Buyer'),
        ('b', 'Requested by Seller'),
        ('1', 'Agreement'),
        ('2', 'Date and Place choosed'),
        ('3', 'Seller meet Buyer in life'),
        ('4', 'Buyer agree to start'),
        ('5', 'Prolongue'),
        ('6', 'Order done'),
        ('7', 'Disput'),
    )

VALUE_CHOICES = (
        ('1', '1 hour'),
        ('2', '2 hours'),
        ('8', 'Night (8 hours)'),
        ('f', "1 Day (24 hours)"),
    )

class Order(models.Model):    

    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Buyer', related_name="buyer")
    seller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Seller', related_name="seller")
    value = models.CharField(max_length=1, choices=VALUE_CHOICES, blank=False, default='2')
    service = models.CharField(max_length=30, choices=SERVICE_CHOICES, blank=False, default='sex')
    active_flag = models.BooleanField(default=True)
    #need rework
    price = models.CharField(max_length=30)

    place = models.CharField(max_length=1, choices=PLACE_CHOICES, blank=False, default='h')
    pay_method = models.CharField(max_length=1, choices=PAY_CHOICES, blank=False, default='b')
    date_ordered = models.DateTimeField(auto_now_add=True, blank=True)
    date_choosen = models.DateTimeField(default=timezone.now(), blank=True)
    
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        blank=True,
        default='a',
        help_text='Current status of Order',
    )

    """docstring for ClassName"""
    def __str__(self):
        return '%s, Buyer: %s, Seller: %s' % (self.service, self.buyer, self.seller)