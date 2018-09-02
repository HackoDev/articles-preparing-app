# Generated by Django 2.1.1 on 2018-09-01 19:48

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название статьи')),
                ('content', markdownx.models.MarkdownxField(default='', verbose_name='HTML текст')),
                ('html_content', models.TextField(default='', verbose_name='HTML текст')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
