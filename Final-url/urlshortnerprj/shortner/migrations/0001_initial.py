# Generated by Django 4.0.2 on 2022-06-11 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=1000)),
                ('uuid', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Urls',
                'verbose_name_plural': 'Urls',
            },
        ),
    ]
