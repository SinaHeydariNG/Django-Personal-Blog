# Generated by Django 4.1 on 2022-09-05 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_services_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteinfo',
            name='email',
            field=models.EmailField(default='imsinacoder@gamil.com', max_length=254),
        ),
    ]
