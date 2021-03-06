# Generated by Django 4.0 on 2022-01-04 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_rename_program_catalogues_program_catalogue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='learnership',
            name='id',
        ),
        migrations.AddField(
            model_name='learnership',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='learnership',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='learnership',
            name='slug',
            field=models.SlugField(default='', max_length=200, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AddField(
            model_name='learnership',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
