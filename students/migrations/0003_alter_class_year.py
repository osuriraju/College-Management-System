# Generated by Django 4.1.3 on 2022-12-06 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_class_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='year',
            field=models.CharField(choices=[('E1', 'E1'), ('E2', 'E2'), ('E3', 'E3'), ('E4', 'E4')], default='E4', max_length=5),
        ),
    ]
