# Generated by Django 2.2.28 on 2024-11-24 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0005_auto_20241124_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='carte',
            name='Pv',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]