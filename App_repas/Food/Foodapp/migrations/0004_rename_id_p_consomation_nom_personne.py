# Generated by Django 4.2 on 2023-05-24 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Foodapp', '0003_consomation_id_p_alter_jour_id_jour'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consomation',
            old_name='id_P',
            new_name='Nom_Personne',
        ),
    ]
