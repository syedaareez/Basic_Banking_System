# Generated by Django 3.2.7 on 2021-09-04 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_users_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sendfrom', models.CharField(max_length=25)),
                ('sendto', models.CharField(max_length=25)),
                ('amount', models.CharField(max_length=25)),
            ],
        ),
    ]
