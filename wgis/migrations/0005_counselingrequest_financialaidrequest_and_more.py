# Generated by Django 5.1.5 on 2025-02-16 01:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wgis', '0004_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='CounselingRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('student_id', models.CharField(max_length=50)),
                ('counseling_type', models.CharField(max_length=50)),
                ('preferred_date', models.DateField()),
                ('preferred_time', models.CharField(max_length=10)),
                ('notes', models.TextField(blank=True)),
                ('submitted_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending', max_length=20)),
            ],
            options={
                'ordering': ['-submitted_at'],
            },
        ),
        migrations.CreateModel(
            name='FinancialAidRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('student_id', models.CharField(max_length=50)),
                ('aid_type', models.CharField(max_length=50)),
                ('academic_year', models.CharField(max_length=10)),
                ('household_income', models.DecimalField(decimal_places=2, max_digits=12)),
                ('documents', models.FileField(blank=True, upload_to='financial_aid_docs/%Y/%m/')),
                ('submitted_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('under_review', 'Under Review'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20)),
            ],
            options={
                'ordering': ['-submitted_at'],
            },
        ),
        migrations.CreateModel(
            name='StudentAffairsInquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('student_id', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('submitted_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('new', 'New'), ('in_progress', 'In Progress'), ('resolved', 'Resolved'), ('closed', 'Closed')], default='new', max_length=20)),
            ],
            options={
                'ordering': ['-submitted_at'],
            },
        ),
    ]
