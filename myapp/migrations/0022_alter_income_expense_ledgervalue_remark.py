# Generated by Django 3.2.7 on 2021-10-13 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_auto_20211013_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income_expense_ledgervalue',
            name='remark',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
