# Generated by Django 4.0.5 on 2022-07-09 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_doctorblog_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(choices=[('Comprehensive', 'Comprehensive Test'), ('Basic Test', 'Basic test')], max_length=50, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('phone_number', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.CharField(choices=[('1', '09:00 - 10:00'), ('2', '10:00 - 11:00'), ('3', '11:00 - 12:00'), ('4', '12:00 - 13:00'), ('5', '13:00 - 14:00')], max_length=50, null=True)),
                ('reason_for_visit', models.CharField(max_length=255, null=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor_appointments', to='core.doctor')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_appointments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
