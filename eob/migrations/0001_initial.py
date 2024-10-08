# Generated by Django 5.1.1 on 2024-10-03 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=200)),
                ('news_content', models.TextField()),
                ('news_image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_title', models.CharField(max_length=200)),
                ('topic_content', models.TextField()),
                ('topic_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
