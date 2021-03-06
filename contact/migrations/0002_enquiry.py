# Generated by Django 4.0 on 2022-01-19 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('cell', models.CharField(max_length=255)),
                ('program_of_interest', models.CharField(max_length=255)),
                ('message', models.TextField(null=True)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
