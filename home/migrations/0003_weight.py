# Generated by Django 3.2.4 on 2022-01-13 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20220112_2048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=32, null=True)),
                ('weight', models.IntegerField(null=True)),
            ],
        ),
    ]
