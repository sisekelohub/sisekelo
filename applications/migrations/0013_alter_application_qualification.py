# Generated by Django 4.0 on 2022-01-06 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0012_remove_qualification_qualification_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='qualification',
            field=models.CharField(choices=[('Matric', 'Matric'), ('Degree', 'Degree'), ('National Diploma', 'National Diploma')], default='Matric', max_length=50),
        ),
    ]
