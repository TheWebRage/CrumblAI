# Generated by Django 3.1.4 on 2020-12-18 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Available',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Cookie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('attributes', models.ManyToManyField(to='ML.Attribute')),
                ('available', models.ManyToManyField(to='ML.Available')),
            ],
        ),
    ]
