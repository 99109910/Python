# Generated by Django 4.1.1 on 2023-08-11 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_aciklama'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='fragman'),
        ),
    ]