# Generated by Django 4.0 on 2022-01-02 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_learnership_certificate_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accredited_program',
            name='mode_of_delivery',
            field=models.CharField(choices=[('Online', 'Online'), ('Physical', 'Physical'), ('Hybrid', 'Hybrid')], default='O', max_length=30),
        ),
    ]
