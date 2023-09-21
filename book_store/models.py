from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(
        blank=False,
        null=False,
        max_length=60
    )
    borrowed_from_date = models.DateField(
        default=timezone.now,
        blank=False,
        null=False,
    )
    borrowed_to_date = models.DateField(
        blank=False,
        null=False,
    )
    is_returned = models.BooleanField(
        default=False,
        blank=True,
        null=False,
    )

    class Meta:
        managed = True
        db_table = "book"
