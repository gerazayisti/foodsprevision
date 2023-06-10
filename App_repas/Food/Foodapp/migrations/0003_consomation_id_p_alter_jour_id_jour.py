# Generated by Django 4.2 on 2023-05-24 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Foodapp', '0002_remove_personne_password_jour_repas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='consomation',
            name='id_P',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Foodapp.personne'),
        ),
        migrations.AlterField(
            model_name='jour',
            name='id_jour',
            field=models.CharField(choices=[('1', 'lundi'), ('2', 'mardi'), ('3', 'mercredi'), ('4', 'jeudi'), ('5', 'vendredi'), ('6', 'samedi'), ('7', 'dimanche')], default=1, help_text='identifiant du jour', max_length=9),
        ),
    ]