# Generated by Django 3.1.6 on 2021-02-08 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210207_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='hospital_image_path',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
