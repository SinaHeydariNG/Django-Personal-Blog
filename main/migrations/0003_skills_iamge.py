# Generated by Django 4.1 on 2022-09-03 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='iamge',
            field=models.ImageField(blank=True, default='img.jpg', upload_to='skills/%y/%m/%d/'),
        ),
    ]