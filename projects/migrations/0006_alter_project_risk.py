# Generated by Django 3.2.8 on 2021-10-23 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_project_risk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='risk',
            field=models.CharField(choices=[('0.05', 'Baixo'), ('0.1', 'Médio'), ('0.2', 'Alto')], max_length=4, verbose_name='Risco'),
        ),
    ]