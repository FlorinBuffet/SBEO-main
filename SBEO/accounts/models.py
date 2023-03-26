from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(
        verbose_name=_('E-Mail adress'),
        max_length=50,
        unique=True)
    birth_date = models.DateField(verbose_name=_('Date of Birth'), null=True)
    mobile = models.CharField(
        max_length=16,
        verbose_name=_('Mobile number'), blank=True)
    allow_Reselection = models.BooleanField(
        default=True,
        verbose_name=_('Allow reselection to similar tournament'))
    street = models.CharField(
        max_length=50,
        verbose_name=_('Street'))
    house_number = models.CharField(
        max_length=10,
        verbose_name=_('House number'))
    postal_code = models.CharField(
        max_length=10,
        verbose_name=_('Postal code'))
    city = models.CharField(
        max_length=50,
        verbose_name=_('City'))
    country = CountryField(
        verbose_name=_('Country'))
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['birth_date']
