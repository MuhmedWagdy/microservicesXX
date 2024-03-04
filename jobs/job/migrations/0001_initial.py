# Generated by Django 5.0.2 on 2024-03-03 12:09

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=20000)),
                ('job_type', models.CharField(choices=[('Internship', 'Internship'), ('PartTime', 'Parttime'), ('Fulltime', 'Fulltime'), ('Contract', 'Contract')], max_length=20)),
                ('education', models.CharField(choices=[('PHD', 'PHD'), ('Master', 'Master'), ('Bachelor', 'Bachelor')], max_length=20)),
                ('experience', models.CharField(choices=[('NoExperience', 'NoExperience'), ('Junior', 'Junior'), ('MidLevel', 'MidLevel'), ('MidSenior', 'MidSenior')], max_length=20)),
                ('salary', models.IntegerField()),
                ('position', models.CharField(max_length=100)),
                ('due_date', models.DateField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('company', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='JobApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('resume', models.CharField(max_length=200)),
                ('cover_letter', models.TextField(max_length=500)),
                ('applied_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applied_job', to='job.job')),
            ],
        ),
    ]
