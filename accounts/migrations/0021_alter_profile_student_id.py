# Generated by Django 4.0 on 2022-02-25 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_alter_profile_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='student_id',
            field=models.CharField(default='2022-8WJT2Y', max_length=32),
        ),
    ]