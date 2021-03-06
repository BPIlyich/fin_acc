# Generated by Django 3.2.4 on 2021-07-01 13:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_add_amount_to_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='initial_amount',
            field=models.DecimalField(decimal_places=2, default=0, help_text='The amount you currently have', max_digits=50, validators=[django.core.validators.MinValueValidator(0)], verbose_name='initial amount'),
        ),
    ]
