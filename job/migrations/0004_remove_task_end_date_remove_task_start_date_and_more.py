# Generated by Django 5.1.3 on 2024-12-17 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_remove_task_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='task',
            name='start_date',
        ),
        migrations.AddField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=0),
            preserve_default=False,
        ),
    ]
