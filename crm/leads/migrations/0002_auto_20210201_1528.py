# Generated by Django 3.1.5 on 2021-02-01 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='avatar',
            field=models.ImageField(null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='lead',
            name='city',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='country',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[('Potential', 'Potential'), ('Prospect', 'Prospect'), ('Negotiation', 'Negotiation'), ('Converted', 'Converted'), ('Failed', 'Failed')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='leads.agent'),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LeadDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(blank=True, upload_to='media')),
                ('tasks', models.TextField(max_length=1000)),
                ('Lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leads.lead')),
            ],
        ),
    ]
