# Generated by Django 2.1.3 on 2018-11-26 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dairyapp', '0007_auto_20181126_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mproduct',
            name='mProduct_qtyunit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dairyapp.mProductUnit'),
        ),
    ]