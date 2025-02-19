# Generated by Django 5.0.4 on 2024-07-01 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caterapp', '0005_buffet_cocktail_corporate_event_wedding'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuDrinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Menu/')),
                ('food_name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('food_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MenuMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Menu/')),
                ('food_name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('food_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MenuOffers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Menu/')),
                ('food_name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('food_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MenuSpecial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Menu/')),
                ('food_name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('food_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MenuStarter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Menu')),
                ('food_name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('food_desc', models.CharField(max_length=100)),
            ],
        ),
    ]
