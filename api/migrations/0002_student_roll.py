# Generated by Django 4.1 on 2022-08-30 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='roll',
            field=models.IntegerField(),
            preserve_default=False,
        ),
    ]
