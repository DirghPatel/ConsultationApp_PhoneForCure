# Generated by Django 3.2.2 on 2021-06-08 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonHealthProblem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.CharField(max_length=200)),
                ('fees', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
