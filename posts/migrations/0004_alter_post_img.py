# Generated by Django 5.0 on 2024-01-26 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(default='./images/Untitled.png', upload_to='images/'),
        ),
    ]
