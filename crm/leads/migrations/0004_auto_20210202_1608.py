# Generated by Django 3.1.5 on 2021-02-02 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_agent_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_company',
            field=models.BooleanField(default=True),
        ),
    ]
