from django.db import models
from django.conf import settings

ROLE = [('1', 'ADMIN'),
        ('2', 'FINANCE_ADMIN'),
        ('3', 'SALES_ADMIN'),
        ('4', 'HR_ADMIN'),
        ('5', 'ENGG_ADMIN'),
        ('0', 'N/A')
        ]


class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    role = models.CharField(max_length=1, choices=ROLE,
                            default='0')
