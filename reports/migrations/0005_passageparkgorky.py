# Generated by Django 4.1.2 on 2022-12-19 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_identsalesbytariff'),
    ]

    operations = [
        migrations.CreateModel(
            name='PassageParkGorky',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_territory', models.CharField(blank=True, max_length=250, null=True)),
                ('count', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]