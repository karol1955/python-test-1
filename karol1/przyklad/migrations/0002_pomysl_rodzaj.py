# Generated by Django 3.0.5 on 2020-04-05 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('przyklad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pomysl',
            name='rodzaj',
            field=models.PositiveSmallIntegerField(choices=[(0, 'zwykly'), (1, 'fajny'), (2, 'superowy')], default=0),
        ),
    ]
