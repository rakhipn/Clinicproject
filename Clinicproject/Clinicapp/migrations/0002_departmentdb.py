# Generated by Django 3.2.10 on 2023-08-01 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clinicapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='departmentdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
