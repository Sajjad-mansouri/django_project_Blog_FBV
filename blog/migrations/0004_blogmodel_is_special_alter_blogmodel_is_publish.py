# Generated by Django 4.1 on 2022-09-06 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogmodel_is_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='is_special',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='is_publish',
            field=models.CharField(choices=[('d', 'پیش نویس'), ('p', 'منتشر شده'), ('i', 'ارسال به مدیر'), ('b', 'نیاز به بررسی بیشتر')], default='d', max_length=1),
        ),
    ]
