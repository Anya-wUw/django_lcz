# Generated by Django 4.0.4 on 2022-05-09 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0002_rename_results_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='score',
            field=models.IntegerField(),
        ),
    ]
