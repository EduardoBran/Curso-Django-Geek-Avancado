# Generated by Django 4.1 on 2022-09-13 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_recurso_alter_funcionario_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='bio',
            field=models.TextField(max_length=200, verbose_name='Bio'),
        ),
    ]
