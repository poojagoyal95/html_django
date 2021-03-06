# Generated by Django 3.1.2 on 2022-04-25 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identification', '0002_auto_20220422_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='code_expert',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='created_preference',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='design_preference',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='final_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='lang_preference',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='map_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='map_preference',
            field=models.IntegerField(null=True),
        ),
    ]
