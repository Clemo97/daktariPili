# Generated by Django 4.0.5 on 2022-07-10 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_patientappointment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientappointment',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
