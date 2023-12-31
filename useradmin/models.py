from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
# Create your models here.

gender_choices = [
    ("M", "Male"),
    ("F", "Female"),
    ("O","Other")
]


role_choices = (
    ('User Admin', 'User Admin'),
    ('Student','Student'),
    ('Staff', 'Staff')
)


class CustomUser(AbstractUser):
    name = models.CharField(max_length=50)
    user_type = models.CharField(choices =  role_choices, max_length = 40)
    father_name = models.CharField(max_length=50)
    gender = models.CharField(choices = gender_choices, max_length=50)
    address = models.CharField(max_length=50)
    # Add related_name to avoid clashes
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_permissions'
    )

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        verbose_name = _('Custom User')
        verbose_name_plural = _('Custom Users')


class useradminmodel(CustomUser):
    im = models.ImageField(upload_to="useradmin")
    descrip = models.CharField(_("Description"), max_length=50)
    join_date = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        verbose_name = _('User-admin')
        verbose_name_plural = _('User-admins')