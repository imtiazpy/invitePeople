from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import CustomUser


# class UserCreationForm(forms.ModelForm):

#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(
#         label='Password Confirm', widget=forms.PasswordInput)

#     class Meta:
#         model = CustomUser
#         fields = ('email', 'name', )

#     def clean_password2(self):
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')

#         if password1 and password2 and password1 != password2:
#             raise ValidationError("Passwords didn't match")
#         return password2

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data)['password1']

#         if commit:
#             user.save()
#         return user
    


# class UserChangeForm(forms.ModelForm):

#     password = ReadOnlyPasswordHashField()

#     class Meta:
#         model = CustomUser
#         fields = ('email', 'password', 'name', 'is_active', 'is_superuser')


# class UserAdmin(BaseUserAdmin):

#     add_form = UserCreationForm
#     change_form = UserChangeForm

#     list_display = ('id', 'email', 'is_active',
#                     'is_superuser', 'is_staff')
#     list_filter = ('is_superuser', 'is_staff', 'is_active')

#     fieldsets = (
#         ('User Info', {'fields': ('email', 'name', 'password')}),
#         ('User Status', {'fields': ('is_superuser', 'is_staff', 'is_active')}),
#     )

#     add_fieldsets = (
#         ('Custom User', {
#             'classes': ('wide', ),
#             'fields': ('email', 'name', 'password1', 'password2'),
#         }),
#     )

#     search_fields = ('email', 'name')
#     ordering = ('email', )


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password Confirm', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'name', )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password didn't match")

        return password2


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data)['password1']

        if commit:
            user.save()

        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'name', 'is_active', 'is_superuser')


class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    change_form = UserChangeForm

    list_display = ('id', 'email', 'is_active', 'is_superuser', 'is_staff')
    list_filter = ('is_superuser', 'is_staff', 'is_active')

    fieldsets = (
        ('User Info', {'fields': ('email', 'name', 'password')}),
        ('User Status', {'fields': ('is_superuser', 'is_staff', 'is_active')}),
    )

    add_fieldsets = (
        ('Custom User', {
            'classes': ('wide', ),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )

    search_fields = ('email', 'name')
    ordering = ('email', )


admin.site.register(CustomUser, UserAdmin)

admin.site.unregister(Group)
