# Generated by Django 3.2.9 on 2022-11-18 20:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_testimonial_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='message',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
