# Generated by Django 5.0.4 on 2024-07-01 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caterapp', '0003_countabout'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=50)),
                ('service_name', models.CharField(max_length=50)),
                ('service_desc', models.CharField(max_length=100)),
            ],
        ),
    ]
