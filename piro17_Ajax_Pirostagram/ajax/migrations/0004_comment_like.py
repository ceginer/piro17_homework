# Generated by Django 4.0.6 on 2022-07-27 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajax', '0003_alter_comment_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='like',
            field=models.BooleanField(default=False, verbose_name='좋아요'),
        ),
    ]