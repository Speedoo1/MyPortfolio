# Generated by Django 3.2.9 on 2022-11-18 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_testimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='message',
            field=models.TextField(),
        ),
    ]
