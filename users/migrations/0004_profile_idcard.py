# Generated by Django 3.0.2 on 2021-01-21 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='idcard',
            field=models.ImageField(default='default.jpg', upload_to='fisrt'),
        ),
    ]
