# Generated by Django 3.0.8 on 2020-07-02 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200702_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='measurement',
            field=models.CharField(default='cup', max_length=30),
            preserve_default=False,
        ),
    ]