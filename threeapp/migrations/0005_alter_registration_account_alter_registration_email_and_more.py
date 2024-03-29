# Generated by Django 4.2.4 on 2024-03-04 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threeapp', '0004_registration_delete_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='account',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='phone_number',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
