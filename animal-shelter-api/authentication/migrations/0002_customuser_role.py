# Generated by Django 5.1 on 2024-08-18 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('adopter', 'Adopter'), ('volunteer', 'Volunteer')], default='adopter', max_length=20),
        ),
    ]
