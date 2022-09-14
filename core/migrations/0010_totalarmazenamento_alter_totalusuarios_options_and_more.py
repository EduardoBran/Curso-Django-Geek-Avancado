# Generated by Django 4.1 on 2022-09-14 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_totalusuarios_alter_preco_usuarios'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalArmazenamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('total', models.CharField(max_length=20, verbose_name='Total de Armazenamento')),
            ],
            options={
                'verbose_name': 'Total de Armazenamento',
                'verbose_name_plural': 'Total de Armazenamento',
            },
        ),
        migrations.AlterModelOptions(
            name='totalusuarios',
            options={'verbose_name': 'Total de Usuário', 'verbose_name_plural': 'Total de Usuários'},
        ),
        migrations.AlterField(
            model_name='totalusuarios',
            name='total',
            field=models.CharField(max_length=20, verbose_name='Total de Usuário'),
        ),
        migrations.AlterField(
            model_name='preco',
            name='armazenamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.totalarmazenamento', verbose_name='Armazenamento'),
        ),
    ]
