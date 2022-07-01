# Generated by Django 3.2.10 on 2022-07-01 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_auto_20220628_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='extra_data',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='order',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]