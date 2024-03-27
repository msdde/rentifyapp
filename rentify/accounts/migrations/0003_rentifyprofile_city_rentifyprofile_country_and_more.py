# Generated by Django 5.0.3 on 2024-03-20 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_rentifyprofile_id_rentifyprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentifyprofile',
            name='city',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='rentifyprofile',
            name='country',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='rentifyprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
    ]