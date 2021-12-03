# Generated by Django 3.2.7 on 2021-10-11 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_rename_society_deatils1_society_all_deatils'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income_Expense_LedgerValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOn', models.DateField()),
                ('type', models.CharField(max_length=100)),
                ('amount', models.FloatField(max_length=100)),
                ('category_header', models.CharField(max_length=100)),
                ('from_or_to_account', models.CharField(max_length=100)),
                ('transaction_type', models.CharField(max_length=100)),
                ('transaction_details', models.CharField(max_length=100)),
                ('voucherNo_or_invoiceNo', models.CharField(max_length=100)),
                ('remark', models.CharField(max_length=500)),
                ('opening_balance_cash', models.FloatField(max_length=100)),
                ('closing_balance_cash', models.FloatField(max_length=100)),
                ('opening_balance_bank', models.FloatField(max_length=100)),
                ('closing_balance_bank', models.FloatField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Society_all_deatils',
        ),
    ]
