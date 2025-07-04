# Generated by Django 5.2 on 2025-05-05 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='Is_Newreleased',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='Is_Toprated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='Is_Trending',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('Horror', 'Horror'), ('action', 'action'), ('romance', 'romance'), ('thriller', 'thriller'), ('drama', 'drama'), ('other', 'other')], default='action', max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='language',
            field=models.CharField(blank=True, choices=[('telugu', 'telugu'), ('english', 'english'), ('hindi', 'hindi'), ('tamil', 'tamil'), ('kannada', 'kannada'), ('other', 'other')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='moviefile',
            field=models.FileField(blank=True, null=True, upload_to='moviefile'),
        ),
    ]
