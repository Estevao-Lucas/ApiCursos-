# Generated by Django 3.1.3 on 2022-01-05 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='celular',
            field=models.CharField(default='', max_length=11),
        ),
    ]
