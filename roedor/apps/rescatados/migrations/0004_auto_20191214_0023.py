# Generated by Django 3.0 on 2019-12-14 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rescatados', '0003_auto_20191214_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='infoM',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Información'),
        ),
    ]
