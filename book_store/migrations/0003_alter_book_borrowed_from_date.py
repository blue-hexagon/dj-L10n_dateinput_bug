# Generated by Django 4.2.5 on 2023-09-28 16:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0002_alter_book_borrowed_from_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='borrowed_from_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
