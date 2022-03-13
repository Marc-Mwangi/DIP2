# Generated by Django 4.0.3 on 2022-03-13 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=1000)),
                ('profile_photo', models.ImageField(upload_to='photos/user_profile')),
                ('profile_slug', models.CharField(max_length=200)),
                ('bio', models.CharField(max_length=4000)),
            ],
        ),
    ]
