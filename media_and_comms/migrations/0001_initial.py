# Generated by Django 4.1.1 on 2023-12-17 13:29

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100, verbose_name='Name')),
                ('body', models.TextField(max_length=255)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Comments',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('image', models.ImageField(upload_to='gallery/')),
            ],
            options={
                'verbose_name_plural': 'Gallery',
            },
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('published_date', models.DateField(verbose_name='Published Date')),
                ('image', models.ImageField(upload_to='podcast/', verbose_name='Image')),
                ('host', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Podcasts',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100, verbose_name='Name')),
                ('body', models.CharField(max_length=150)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('parent_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='media_and_comms.comment')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('published_date', models.DateField(verbose_name='Published Date')),
                ('author', models.CharField(max_length=250, verbose_name='Author')),
                ('image', models.ImageField(blank=True, null=True, upload_to='releases/', verbose_name='Image')),
                ('document', models.FileField(blank=True, null=True, upload_to='', verbose_name='Document')),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name_plural': 'Releases',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('published_date', models.DateField(verbose_name='Published Date')),
                ('posted_by', models.CharField(max_length=250, verbose_name='Posted By')),
                ('image', models.ImageField(upload_to='news/', verbose_name='Image')),
                ('url', models.URLField()),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name_plural': 'News',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='parent_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='media_and_comms.release'),
        ),
    ]
