# Generated by Django 4.0 on 2022-01-09 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_carousel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carousel',
            name='image_url',
        ),
        migrations.AddField(
            model_name='carousel',
            name='description',
            field=models.TextField(max_length=50, null=True),
        ),
    ]
