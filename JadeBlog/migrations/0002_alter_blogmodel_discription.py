# Generated by Django 3.2.15 on 2022-09-20 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JadeBlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='discription',
            field=models.TextField(max_length=600),
        ),
    ]