# Generated by Django 3.2.2 on 2021-06-23 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0008_alter_bookappointment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookappointment',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
