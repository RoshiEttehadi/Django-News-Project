# Generated by Django 3.0.8 on 2020-08-08 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200805_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
