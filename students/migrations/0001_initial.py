# Generated by Django 4.1.3 on 2022-12-06 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(choices=[('ME', 'ME'), ('CSE', 'CSE'), ('ECE', 'ECE'), ('CHE', 'CHE'), ('CE', 'CE'), ('MME', 'MME')], max_length=5)),
                ('year', models.CharField(choices=[('E1', 'E1'), ('E2', 'E2'), ('E3', 'E3'), ('E4', 'E4')], max_length=5)),
                ('classname', models.CharField(max_length=10)),
            ],
        ),
    ]