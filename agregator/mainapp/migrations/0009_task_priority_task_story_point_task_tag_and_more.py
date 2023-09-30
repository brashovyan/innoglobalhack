# Generated by Django 4.2.5 on 2023-09-30 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_user_master_user_profession_user_story_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='story_point',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mainapp.profession'),
        ),
        migrations.AlterField(
            model_name='project',
            name='owners',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]