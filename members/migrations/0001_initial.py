# Generated by Django 4.1.1 on 2022-10-11 05:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('account_type', models.CharField(max_length=255)),
                ('account_status', models.CharField(max_length=255)),
                ('wallet_balance', models.FloatField()),
                ('invested', models.FloatField()),
                ('total_withdrawal', models.FloatField()),
                ('referral_bonus', models.FloatField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
