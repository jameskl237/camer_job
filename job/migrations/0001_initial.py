# Generated by Django 5.1.3 on 2024-11-28 14:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('Price', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('place', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('FR', 'Free'), ('D', 'During'), ('FN', 'Finish')], default='FR', max_length=20)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='job.domain')),
            ],
        ),
    ]