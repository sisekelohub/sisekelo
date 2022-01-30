# Generated by Django 4.0 on 2022-01-02 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Highest_qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('mid_name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('equity', models.CharField(choices=[('B', 'Black'), ('C', 'Colored'), ('I', 'Indian'), ('W', 'White'), ('O', 'Other')], default='B', max_length=30)),
                ('disability', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=30)),
                ('street_address', models.CharField(max_length=255)),
                ('street_address2', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=14)),
                ('whatsapp', models.CharField(max_length=14)),
                ('work_phone', models.CharField(max_length=14)),
                ('south_african_citizen', models.CharField(choices=[('yes', 'Yes'), ('asylum', 'Asylum'), ('visa', 'Visa')], max_length=30)),
                ('non_citizen_docs', models.FileField(upload_to='uploads/non_citizen_docs/')),
                ('nk_name', models.CharField(max_length=255)),
                ('nk_surname', models.CharField(max_length=255)),
                ('nk_home_tel', models.CharField(max_length=255)),
                ('nk_cellphone', models.CharField(max_length=255)),
                ('nk_email', models.EmailField(max_length=254)),
                ('name_of_employer', models.CharField(max_length=255)),
                ('comments', models.TextField(null=True)),
                ('agreement', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=30)),
                ('highest_qualification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applications.highest_qualification')),
            ],
        ),
    ]
