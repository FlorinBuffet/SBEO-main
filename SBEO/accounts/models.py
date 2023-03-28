from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, birth_date, mobile, street, house_number,
                    postal_code, city, country, password=None):
        if not email:
            raise ValueError("User must have an email adress")

        user = self.model(
            email=self.normalize_email(email),
            birth_date=birth_date,
            mobile=mobile,
            street=street,
            house_number=house_number,
            postal_code=postal_code,
            city=city,
            country=country,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, birth_date, mobile, street, house_number,
                         postal_code, city, country, password=None):
        superuser = self.create_user(
            email,
            password=password,
            birth_date=birth_date,
            mobile=mobile,
            street=street,
            house_number=house_number,
            postal_code=postal_code,
            city=city,
            country=country,
        )

        superuser.is_admin = True
        superuser.save(using=self._db)
        return superuser


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name=_('E-Mail adress'),
        max_length=50,
        unique=True)
    first_name = models.CharField(max_length=50, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=50, verbose_name=_('Last Name'))
    birth_date = models.DateField(verbose_name=_('Date of Birth'), null=True)
    mobile = models.CharField(
        max_length=16,
        verbose_name=_('Mobile number'))
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
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['birth_date', 'mobile', 'street',
                       'house_number', 'postal_code', 'city', 'country']
    is_admin = models.BooleanField(default=False, verbose_name=_('Is Admin'))

    @property
    def is_staff(self):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, app_label):
        return True

    objects = UserManager()

    def __str__(self):
        return self.email
