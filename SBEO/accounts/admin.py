from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from django.core.exceptions import ValidationError

from .models import User


class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['first_name','last_name','email','password','birth_date']

class UserCreationForm(forms.ModelForm):

    password1=forms.CharField(label='Password', widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email','password','birth_date']
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user



class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ['last_name', 'first_name', 'email', 'is_admin']
    list_filter = ['is_admin']
    fieldsets = [
        (None, {'fields': ['first_name', 'last_name', 'email', 'password']}),
        ('Personal info', {'fields': ['birth_date', 'street', 'house_number', 'postal_code', 'city', 'country']}),
        ('Permissions', {'fields': ['is_admin']}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['email', 'birth_date', 'password1', 'password2'],
            },
        ),
    ]
    search_fields = ['email', 'first_name', 'last_name']
    ordering = ['last_name', 'first_name']
    filter_horizontal = []

# Register your models here.
admin.site.register(User, UserAdmin)
