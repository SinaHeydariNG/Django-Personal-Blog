# Generated by Django 4.1 on 2022-09-04 07:16

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('subtitle', models.CharField(max_length=225)),
                ('image', models.ImageField(upload_to='blog/%y/%m/%d/')),
                ('image_1', models.ImageField(blank=True, upload_to='blog/%y/%m/%d/')),
                ('image_2', models.ImageField(blank=True, upload_to='blog/%y/%m/%d/')),
                ('image_3', models.ImageField(blank=True, upload_to='blog/%y/%m/%d/')),
                ('image_4', models.ImageField(blank=True, upload_to='blog/%y/%m/%d/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateField(auto_now_add=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.category')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
