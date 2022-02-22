# Generated by Django 4.0 on 2022-02-16 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_db', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookcopy',
            old_name='book_id',
            new_name='book_key',
        ),
        migrations.AlterUniqueTogether(
            name='bookcopy',
            unique_together={('book_key', 'copy_number')},
        ),
    ]