# Generated by Django 5.0.4 on 2024-07-01 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caterapp', '0011_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.CharField(max_length=50)),
            ],
        ),
    ]
