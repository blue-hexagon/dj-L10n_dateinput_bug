# Generated by Django 4.2.5 on 2023-09-28 16:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0003_alter_book_borrowed_from_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='borrowed_from_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
