# Generated by Django 3.1.7 on 2021-03-09 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arts', '0005_auto_20210301_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arts',
            name='action',
            field=models.CharField(choices=[('UDNIE', 'Udnie'), ('CANDY', 'Candy'), ('MOSAIC', 'Mosaic'), ('PINK', 'Pink'), ('LA_MUSE', 'La Muse'), ('RAIN', 'Rain'), ('LANDSCAPE', 'Landscape'), ('TRIANGLE', 'Triangle')], max_length=50),
        ),
    ]
