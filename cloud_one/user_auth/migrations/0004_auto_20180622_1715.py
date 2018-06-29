# Generated by Django 2.0.6 on 2018-06-22 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0003_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='description',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='account',
            name='website',
            field=models.URLField(null=True),
        ),
    ]
