# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-06 14:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import weblate.utils.render


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0010_auto_20181205_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='merge_message',
            field=models.TextField(default=settings.DEFAULT_MERGE_MESSAGE, help_text='You can use template language for various info, please consult the documentation for more details.', validators=[weblate.utils.render.validate_render_component], verbose_name='Commit message when merging translation'),
        ),
    ]
