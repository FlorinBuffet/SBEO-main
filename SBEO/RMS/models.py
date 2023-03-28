from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

# Create your models here.


class Location(models.Model):
    """
    Class to store a Location with following fields:
    name: Char Field which represents a given name of a Location
    club: Char Field which stands for the club which owns the Location
    street: Char Field for a Street Name
    house_numner: Char Field for a House Number
    postal_code: Char Field for a Postal Code
    city: Char Field for the City
    Country: CountryField which is configured in /SBEO/SBEO/settings.py
    comment: Text Field for comments like Parking etc
    is_deleted: Boolean for hiding a location in the selection
    """
    
    name = models.CharField(
        max_length=150,
        verbose_name=_('Location Name'))
    club = models.CharField(
        max_length=250,
        verbose_name=_('Club Name'))
    street = models.CharField(
        max_length=80,
        verbose_name=_('Street'))
    house_number = models.CharField(
        max_length=5,
        verbose_name=_('House number'))
    postal_code = models.CharField(
        max_length=10,
        verbose_name=_('Postal code'))
    city = models.CharField(
        max_length=50,
        verbose_name=_('City'))
    country = CountryField(
        verbose_name=_('Country'))
    comment = models.TextField(
        blank=True,
        verbose_name=_('Comment'))
    is_deleted = models.BooleanField(
        default=False,
        verbose_name=_('Deleted'))

    def __str__(self):
        return self.club + ": " + self.name


class Event(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Event Name'))
    location = models.ForeignKey(
        Location,
        on_delete=models.PROTECT,
        verbose_name=_('Location'))
    start_date = models.DateTimeField(verbose_name=_('Start Date'))
    start_time = models.TimeField(verbose_name=_('Start Time'))
    end_date = models.DateTimeField(verbose_name=_('End Date'))
    persons_needed = models.IntegerField(verbose_name=_('Persons needed'))
    fee_per_person = models.IntegerField(verbose_name=_('Fees per Person'))
    notes = models.TextField(verbose_name=_('Additional Notes'))
    link1_link = models.URLField(verbose_name=_('Link 1 URL'))
    link1_name = models.CharField(
        max_length=50,
        verbose_name=_('Link 1 Name'))
    link2_link = models.URLField(verbose_name=_('Link 2 URL'))
    link2_name = models.CharField(
        max_length=50,
        verbose_name=_('Link 2 Name'))
    link3_link = models.URLField(verbose_name=_('Link 3 URL'))
    link3_name = models.CharField(
        max_length=50,
        verbose_name=_('Link 3 Name'))
    link4_link = models.URLField(verbose_name=_('Link 4 URL'))
    link4_name = models.CharField(
        max_length=50,
        verbose_name=_('Link 4 Name'))
    link5_link = models.URLField(verbose_name=_('Link 5 URL'))
    link5_name = models.CharField(
        max_length=50,
        verbose_name=_('Link 5 Name'))

    def __str__(self):
        return f"{ self.name }"


class Registration(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.PROTECT,
        verbose_name=_('Event'))
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name=_('User'))


class Invitation(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.PROTECT,
        verbose_name=_('Name')
    )
    invitees = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name=_('Invitations'),
        related_query_name='invitations',
        verbose_name=_('Inivitees for Event')
    )
    # The Invitation is official and not only temporary
    is_official = models.BooleanField(verbose_name=_('Selection official'))
    head_referee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name=_('Headreferee for Event'))
    message = models.TextField(
        verbose_name=_('Message')
    )
