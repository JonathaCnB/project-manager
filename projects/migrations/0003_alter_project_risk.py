# Generated by Django 3.2.8 on 2021-10-22 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_rename_correct_answer_project_risk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='risk',
            field=models.CharField(choices=[('0', 'Baixo'), ('1', 'Médio'), ('2', 'Alto')], max_length=1, verbose_name='Risco'),
        ),
    ]