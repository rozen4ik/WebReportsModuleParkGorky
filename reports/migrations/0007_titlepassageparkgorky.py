# Generated by Django 4.1.2 on 2022-12-22 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_remove_passagesturnstile_id_ter_from_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TitlePassageParkGorky',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
