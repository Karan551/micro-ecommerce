# Generated by Django 5.1.3 on 2024-11-28 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productattachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='productattachment',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]