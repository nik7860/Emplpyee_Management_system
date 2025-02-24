# Generated by Django 5.0.6 on 2024-10-13 14:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='employee_education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epg', models.CharField(max_length=100, null=True)),
                ('colpg', models.CharField(max_length=200, null=True)),
                ('perpg', models.CharField(max_length=30, null=True)),
                ('ypg', models.CharField(max_length=30, null=True)),
                ('eg', models.CharField(max_length=100, null=True)),
                ('colg', models.CharField(max_length=200, null=True)),
                ('perg', models.CharField(max_length=30, null=True)),
                ('yg', models.CharField(max_length=30, null=True)),
                ('ess', models.CharField(max_length=100, null=True)),
                ('colss', models.CharField(max_length=200, null=True)),
                ('perss', models.CharField(max_length=30, null=True)),
                ('yss', models.CharField(max_length=30, null=True)),
                ('eh', models.CharField(max_length=100, null=True)),
                ('colh', models.CharField(max_length=200, null=True)),
                ('perh', models.CharField(max_length=30, null=True)),
                ('yh', models.CharField(max_length=30, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='employee_experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company1', models.CharField(max_length=200, null=True)),
                ('company1_des', models.CharField(max_length=200, null=True)),
                ('company1_salary', models.CharField(max_length=100, null=True)),
                ('company1dur', models.CharField(max_length=100, null=True)),
                ('company2', models.CharField(max_length=200, null=True)),
                ('company2_des', models.CharField(max_length=200, null=True)),
                ('company2_salary', models.CharField(max_length=100, null=True)),
                ('company2dur', models.CharField(max_length=100, null=True)),
                ('company3', models.CharField(max_length=200, null=True)),
                ('company3_des', models.CharField(max_length=200, null=True)),
                ('company3_salary', models.CharField(max_length=100, null=True)),
                ('company3dur', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
