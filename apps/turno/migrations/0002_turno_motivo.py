# Generated by Django 2.2.3 on 2019-10-31 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turno', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='turno',
            name='motivo',
            field=models.CharField(choices=[('Escolar', 'Escolar'), ('Personal', 'Personal')], default='Escolar', max_length=1),
        ),
    ]
