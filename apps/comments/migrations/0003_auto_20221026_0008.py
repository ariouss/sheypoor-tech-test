# Generated by Django 3.2.16 on 2022-10-26 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_alter_comment_parent_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='deleted_at',
        ),
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
