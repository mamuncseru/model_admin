# Generated by Django 2.2.7 on 2019-11-12 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='complain',
            new_name='complaint',
        ),
    ]