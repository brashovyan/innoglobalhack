# Generated by Django 4.2.5 on 2023-09-30 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profession',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sprint',
            name='date_end',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='sprint',
            name='date_start',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='sprint',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='sprint',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mainapp.project'),
        ),
        migrations.AlterField(
            model_name='sprint',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='sprint',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='sprint',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mainapp.sprint'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default='ToDo', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
