# Generated by Django 3.2.9 on 2022-11-19 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_myfield'),
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(null=True, upload_to='')),
                ('company_name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]