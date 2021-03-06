# Generated by Django 2.2 on 2021-01-26 09:15

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_promote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='cover',
            field=models.FileField(upload_to='article_cover/', validators=[blog.models.validate_file_ext]),
        ),
        migrations.AlterField(
            model_name='category',
            name='cover',
            field=models.FileField(upload_to='category_cover/', validators=[blog.models.validate_file_ext]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.FileField(upload_to='user_avatar/', validators=[blog.models.validate_file_ext]),
        ),
    ]
