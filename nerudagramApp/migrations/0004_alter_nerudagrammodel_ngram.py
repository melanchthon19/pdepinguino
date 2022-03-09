# Generated by Django 4.0.2 on 2022-03-02 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nerudagramApp', '0003_alter_nerudagrammodel_ngram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nerudagrammodel',
            name='ngram',
            field=models.IntegerField(choices=[(1, 'monograma'), (2, 'bigrama'), (3, 'trigrama'), (4, 'tetragrama')]),
        ),
    ]
