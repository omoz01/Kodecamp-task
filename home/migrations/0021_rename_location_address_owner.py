# Generated by Django 4.0.4 on 2022-06-05 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_remove_people_fname_remove_people_lname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='location',
            new_name='owner',
        ),
    ]
