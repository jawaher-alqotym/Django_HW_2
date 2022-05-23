# Generated by Django 4.0.4 on 2022-05-23 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='the name of the project', max_length=100)),
                ('creation_time', models.DateTimeField(auto_now_add=True, help_text='this is creation time')),
                ('completion_time', models.DateTimeField(help_text='this is completion time', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='this is task name', max_length=100)),
                ('description', models.TextField(help_text='this is task description')),
                ('time_estimate', models.IntegerField(help_text='this is the time a task might take')),
                ('completed', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMApp.project')),
            ],
        ),
    ]