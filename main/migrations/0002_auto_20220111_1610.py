# Generated by Django 3.2.11 on 2022-01-11 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='live_demo',
            field=models.URLField(default='123', help_text='Url link of live webpage'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='source_file',
            field=models.URLField(default=123, help_text='Link to source code'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='madeWith',
            field=models.CharField(help_text='Technologies used for building  a project', max_length=240),
        ),
        migrations.AlterField(
            model_name='project',
            name='paragraph',
            field=models.TextField(help_text='Full discription of the project. Use HTML tags to style a text.'),
        ),
    ]
