# Generated by Django 5.1.5 on 2025-01-26 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='foto_perfil',
            field=models.ImageField(blank=True, default='fotos_perfil/default_profile.png', null=True, upload_to='fotos_perfil/'),
        ),
    ]
