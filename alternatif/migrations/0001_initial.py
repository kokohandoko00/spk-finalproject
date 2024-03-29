# Generated by Django 3.0.4 on 2020-03-30 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alternatif',
            fields=[
                ('kodealternatif', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('namaalternatif', models.CharField(max_length=25)),
                ('c1', models.IntegerField()),
                ('c2', models.IntegerField(choices=[(1, '< 0℃'), (2, '0℃ - 15℃'), (3, '> 15℃')], default=1, max_length=1)),
                ('c3', models.IntegerField(choices=[(1, 'KURANG MENDUKUNG'), (2, 'CUKUP MENDUKUNG'), (3, 'SANGAT MENDUKUNG')], default=1, max_length=1)),
                ('c4', models.IntegerField(choices=[(1, '< 40'), (2, '40 - 60'), (3, '> 60')], default=1, max_length=1)),
                ('c5', models.IntegerField(choices=[(1, '< Rp 3.000.000'), (2, 'Rp 3.000.000 - Rp 5.000.000'), (3, '> Rp 5.000.000')], default=1, max_length=1)),
            ],
        ),
    ]
