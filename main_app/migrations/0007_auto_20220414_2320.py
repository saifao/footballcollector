# Generated by Django 2.2.12 on 2022-04-14 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20220414_0007'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wage',
            options={'ordering': ['-payday']},
        ),
        migrations.AlterField(
            model_name='player',
            name='contract_exp',
            field=models.DateField(verbose_name='Contract Expiration'),
        ),
        migrations.AlterField(
            model_name='player',
            name='mkt_value',
            field=models.IntegerField(verbose_name='Market Value'),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Player Name'),
        ),
        migrations.AlterField(
            model_name='wage',
            name='amount',
            field=models.IntegerField(default=0, verbose_name='Salary Amount'),
        ),
        migrations.AlterField(
            model_name='wage',
            name='payday',
            field=models.DateField(verbose_name='Date Paid'),
        ),
    ]
