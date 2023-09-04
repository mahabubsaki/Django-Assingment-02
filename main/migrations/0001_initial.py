# Generated by Django 4.2.4 on 2023-09-04 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=255)),
                ('taskDescription', models.TextField()),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]
