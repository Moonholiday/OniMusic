# Generated by Django 3.2 on 2022-04-14 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_rename_genre_img_category_category_img'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Genre',
        ),
        migrations.RenameField(
            model_name='genre',
            old_name='category_img',
            new_name='genre_img',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='category',
            new_name='genre',
        ),
    ]
