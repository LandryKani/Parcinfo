# Generated by Django 4.0.4 on 2022-05-17 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorie',
            name='id',
        ),
        migrations.AlterField(
            model_name='categorie',
            name='nomc',
            field=models.CharField(max_length=200, primary_key='nomc', serialize=False),
        ),
    ]
