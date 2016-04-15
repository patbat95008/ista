# Copyright 2016 by Dane Collins
from django.db import models


class TestSession(models.Model):
    STANDARD = 'STANDARD'
    SMALL = 'SMALL'
    FLAT = 'FLAT'
    ELONGATED = 'ELONGATED'
    TYPE_CHOICES = (
        (STANDARD, 'Standard'),
        (SMALL, 'Small'),
        (FLAT, 'Flat'),
        (ELONGATED, 'Elongated')
    )

    item_name = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    package_type = models.CharField(max_length=9, choices=TYPE_CHOICES, default=STANDARD)
    test = models.CharField(max_length=10)

