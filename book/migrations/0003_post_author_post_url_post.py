# Generated by Django 4.1.7 on 2023-03-19 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='url_post',
            field=models.URLField(null=True),
        ),
    ]
