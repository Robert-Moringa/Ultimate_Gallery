# Generated by Django 3.2.6 on 2021-09-04 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ultimate_gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='image_path',
        ),
    ]
