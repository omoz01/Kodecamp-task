# Generated by Django 4.0.4 on 2022-06-01 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_post_author_alter_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='Username',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
