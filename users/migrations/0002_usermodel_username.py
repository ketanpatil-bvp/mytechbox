# Generated by Django 3.1.2 on 2020-10-17 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='username',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
