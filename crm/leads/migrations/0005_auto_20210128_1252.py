# Generated by Django 3.1.5 on 2021-01-28 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0004_lead_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]