# Generated by Django 3.2.5 on 2021-07-19 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('luna', '0003_rename_usuarios_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad', models.CharField(max_length=30)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luna.usuario')),
            ],
        ),
    ]
