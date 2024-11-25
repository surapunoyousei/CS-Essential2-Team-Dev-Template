from django.db import models

# Create your models here.

from django.db import models
# Create your models here.

class User_Model(models.Model):

    class Meta:
        db_table = 'User'

    user_id = models.CharField(
        verbose_name='userid',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    user_name = models.CharField(
        verbose_name='username',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    user_email = models.CharField(
        verbose_name='useremail',
        blank=True,
        null=True,
        max_length=225,
        default='',
    )

    def __str__(self):
        return self.user_id