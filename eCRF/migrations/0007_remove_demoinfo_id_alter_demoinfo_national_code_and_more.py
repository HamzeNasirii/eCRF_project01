# Generated by Django 4.0.2 on 2022-08-06 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eCRF', '0006_demoinfo_datetime_created_demoinfo_datetime_modified_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demoinfo',
            name='id',
        ),
        migrations.AlterField(
            model_name='demoinfo',
            name='national_code',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='healthinfo',
            name='national_code',
            field=models.ForeignKey(blank=True, default=7944229289, on_delete=django.db.models.deletion.CASCADE, related_name='health', to='eCRF.demoinfo'),
        ),
    ]
