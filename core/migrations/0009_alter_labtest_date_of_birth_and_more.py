# Generated by Django 4.0.5 on 2022-07-10 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_patientappointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labtest',
            name='date_of_birth',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='patientappointment',
            name='date',
            field=models.DateTimeField(),
        ),
    ]