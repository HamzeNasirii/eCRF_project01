# Generated by Django 4.0.2 on 2022-07-31 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eCRF', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfoaddress',
            name='national_code',
            field=models.ForeignKey(default=1234567890, on_delete=django.db.models.deletion.CASCADE, to='eCRF.demoinfo'),
        ),
        migrations.AddField(
            model_name='contactinfophone',
            name='national_code',
            field=models.ForeignKey(default=1234567890, on_delete=django.db.models.deletion.CASCADE, to='eCRF.demoinfo'),
        ),
        migrations.AddField(
            model_name='healthinfo',
            name='national_code',
            field=models.ForeignKey(default=1234567890, on_delete=django.db.models.deletion.CASCADE, to='eCRF.demoinfo'),
        ),
    ]
