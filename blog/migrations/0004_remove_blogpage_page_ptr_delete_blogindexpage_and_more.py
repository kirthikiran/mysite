# Generated by Django 4.1.3 on 2022-11-28 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogindexpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='BlogIndexPage',
        ),
        migrations.DeleteModel(
            name='BlogPage',
        ),
    ]
