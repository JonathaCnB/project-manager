# Generated by Django 3.2.8 on 2021-10-23 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_risk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='risk',
            field=models.CharField(choices=[('05', 'Baixo'), ('1', 'Médio'), ('2', 'Alto')], max_length=2, verbose_name='Risco'),
        ),
    ]
