# Generated by Django 4.1.3 on 2022-12-06 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='idnum',
            field=models.CharField(default=123, max_length=10),
            preserve_default=False,
        ),
    ]