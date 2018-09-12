# Generated by Django 2.1 on 2018-09-03 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_auto_20180819_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruta_name', models.CharField(max_length=250)),
                ('is_favorite', models.BooleanField(default=False)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Song')),
            ],
        ),
    ]
