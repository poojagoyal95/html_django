# Generated by Django 3.1.2 on 2022-04-25 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identification', '0004_auto_20220425_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='final_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='map_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
