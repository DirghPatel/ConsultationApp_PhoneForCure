# Generated by Django 3.2.2 on 2021-06-22 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_bookappointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookappointment',
            name='status',
            field=models.CharField(default=False, max_length=100),
        ),
    ]
