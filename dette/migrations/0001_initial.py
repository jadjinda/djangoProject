# Generated by Django 5.1.2 on 2024-12-11 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('montantTotal', models.DecimalField(decimal_places=2, max_digits=65)),
                ('montantRestant', models.DecimalField(decimal_places=2, max_digits=65)),
                ('dateEcheance', models.DateField()),
            ],
        ),
    ]