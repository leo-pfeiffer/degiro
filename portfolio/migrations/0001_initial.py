# Generated by Django 3.1.2 on 2021-05-07 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isin', models.CharField(max_length=12, verbose_name='ISIN')),
                ('symbol', models.CharField(max_length=100, verbose_name='Stock market symbol')),
                ('name', models.TextField(verbose_name='Asset name')),
                ('type', models.CharField(max_length=32, verbose_name='Asset type')),
                ('currency', models.CharField(max_length=3, verbose_name='Asset currency')),
                ('productId', models.CharField(max_length=32, verbose_name='Degiro product ID')),
            ],
        ),
        migrations.CreateModel(
            name='Cashflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True, verbose_name='Date')),
                ('cashflow', models.FloatField(verbose_name='Value of the Cashflow')),
            ],
        ),
        migrations.CreateModel(
            name='Depot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pieces', models.FloatField(verbose_name='Number of pieces of the symbol')),
            ],
        ),
        migrations.CreateModel(
            name='DimensionSymbolDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=100, verbose_name='Stock market symbol')),
                ('date', models.DateField(verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False, verbose_name='Transaction ID')),
                ('productId', models.CharField(max_length=32, verbose_name='Degiro product ID of associated product')),
                ('date', models.DateField(verbose_name='Date')),
                ('buysell', models.CharField(max_length=1, verbose_name='Buy or Sell transaction')),
                ('price', models.FloatField(blank=True, default=None, null=True, verbose_name='Price of the underlying asset')),
                ('quantity', models.FloatField(blank=True, default=None, null=True, verbose_name='Quantity of the underlying asset')),
                ('total', models.FloatField(blank=True, default=None, null=True, verbose_name='Total value of the transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0, verbose_name='Price of the asset on the date')),
                ('symbol_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.dimensionsymboldate')),
            ],
        ),
        migrations.AddConstraint(
            model_name='dimensionsymboldate',
            constraint=models.UniqueConstraint(fields=('symbol', 'date'), name='unique_symbol_date'),
        ),
        migrations.AddField(
            model_name='depot',
            name='symbol_date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.dimensionsymboldate'),
        ),
    ]