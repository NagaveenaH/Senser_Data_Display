# Generated by Django 3.0.5 on 2020-09-02 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='store_extract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reading', models.FloatField()),
                ('timestamp', models.PositiveIntegerField()),
                ('sensor_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='D1',
        ),
    ]
