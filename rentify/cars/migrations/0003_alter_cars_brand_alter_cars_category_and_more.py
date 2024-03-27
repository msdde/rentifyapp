# Generated by Django 5.0.3 on 2024-03-22 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_cars_brand_alter_cars_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='brand',
            field=models.CharField(choices=[('BMW', 'BMW'), ('Mercedes', 'Mercedes'), ('Audi', 'Audi')], max_length=20),
        ),
        migrations.AlterField(
            model_name='cars',
            name='category',
            field=models.CharField(choices=[('SUV', 'SUV'), ('Compact', 'Compact'), ('EV', 'EV')], max_length=20),
        ),
        migrations.AlterField(
            model_name='cars',
            name='gearbox',
            field=models.CharField(choices=[('Manual', 'Manual'), ('Auto', 'Auto')], max_length=20),
        ),
    ]