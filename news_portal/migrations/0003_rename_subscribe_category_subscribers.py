# Generated by Django 4.1.7 on 2023-04-02 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_portal', '0002_category_subscribe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='subscribe',
            new_name='subscribers',
        ),
    ]