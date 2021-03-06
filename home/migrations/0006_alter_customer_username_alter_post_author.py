# Generated by Django 4.0.4 on 2022-06-01 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Username',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.customer'),
        ),
    ]
