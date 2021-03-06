# Generated by Django 3.2.7 on 2021-10-06 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_remove_income_expense_ledger_entry_date_and_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Society_deatils1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('contact_name', models.CharField(max_length=500)),
                ('otp', models.IntegerField(default=459)),
                ('moblie_no', models.CharField(max_length=10, unique=True)),
                ('society_name', models.CharField(max_length=500)),
                ('society_address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=200)),
                ('pin_code', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=100)),
                ('society_registration_number', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('is_verfied', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
