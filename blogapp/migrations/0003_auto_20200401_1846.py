# Generated by Django 3.0.2 on 2020-04-01 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20200331_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('Publish', 'Publish'), ('Repost', 'Repost')], default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=True, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]