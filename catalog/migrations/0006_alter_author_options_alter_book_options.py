# Generated by Django 4.1.7 on 2023-02-22 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_bookinstance_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name']},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title', 'author']},
        ),
    ]
