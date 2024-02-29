# Generated by Django 4.1.1 on 2023-08-11 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=30)),
                ('resim', models.FileField(upload_to='filmler', verbose_name='Film ismi giriniz')),
            ],
        ),
    ]
