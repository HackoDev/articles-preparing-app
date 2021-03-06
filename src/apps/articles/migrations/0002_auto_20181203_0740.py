# Generated by Django 2.1.2 on 2018-12-03 07:40

from django.db import migrations, models
import django.db.models.deletion
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'article', 'verbose_name_plural': 'articles'},
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=markdownx.models.MarkdownxField(default='', verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='article',
            name='html_content',
            field=models.TextField(default='', editable=False, verbose_name='compiled HTML content'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=128, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, default=None, on_delete=django.db.models.deletion.PROTECT, related_name='articles', to='articles.Category', verbose_name='category'),
        ),
    ]
