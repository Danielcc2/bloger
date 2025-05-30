# Generated by Django 5.2.1 on 2025-05-18 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('reader', 'Lector'), ('writer', 'Escritor'), ('admin', 'Administrador')], default='reader', help_text='Rol del usuario que determina sus permisos en la plataforma', max_length=20),
        ),
    ]
