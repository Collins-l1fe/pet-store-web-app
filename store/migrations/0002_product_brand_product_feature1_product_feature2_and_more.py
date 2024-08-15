# Generated by Django 4.2 on 2024-05-02 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='brand', max_length=155),
        ),
        migrations.AddField(
            model_name='product',
            name='feature1',
            field=models.CharField(default='feature', max_length=155),
        ),
        migrations.AddField(
            model_name='product',
            name='feature2',
            field=models.CharField(default='feature', max_length=155),
        ),
        migrations.AddField(
            model_name='product',
            name='feature3',
            field=models.CharField(default='feature', max_length=155),
        ),
        migrations.AddField(
            model_name='product',
            name='feature4',
            field=models.CharField(default='feature', max_length=155),
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(max_length=155, null=True),
        ),
    ]
