# Generated by Django 4.2.6 on 2023-11-01 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='full_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contactsupport',
            name='subject',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contactsupport',
            name='username',
            field=models.CharField(max_length=255),
        ),
    ]
