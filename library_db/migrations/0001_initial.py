# Generated by Django 4.0 on 2022-02-15 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('publish_date', models.DateField()),
                ('number_of_pages', models.IntegerField()),
            ],
            options={
                'unique_together': {('title', 'author')},
            },
        ),
        migrations.CreateModel(
            name='BookCopy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copy_number', models.IntegerField()),
                ('book_in', models.BooleanField(default=True)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_db.book')),
            ],
            options={
                'unique_together': {('book_id', 'copy_number')},
            },
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_checkout', models.DateField()),
                ('due_date', models.DateField()),
                ('date_of_checkin', models.DateField()),
                ('book_copy', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='library_db.bookcopy')),
            ],
        ),
        migrations.CreateModel(
            name='LibraryUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('status', models.CharField(choices=[('excellent', 'excellent'), ('good', 'good'), ('probationary', 'probationary')], default='good', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='LibraryAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('librarian_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_db.libraryuser')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkout', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='library_db.checkout')),
            ],
        ),
        migrations.AddField(
            model_name='checkout',
            name='librarian_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='library_db.librarian'),
        ),
        migrations.AddField(
            model_name='checkout',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='library_db.libraryuser'),
        ),
    ]
