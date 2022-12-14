# Generated by Django 4.0.2 on 2022-08-07 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eCRF', '0007_remove_demoinfo_id_alter_demoinfo_national_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demoinfo',
            name='country',
        ),
        migrations.AlterField(
            model_name='contactinfoaddress',
            name='national_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contactadd', to='eCRF.demoinfo'),
        ),
        migrations.AlterField(
            model_name='contactinfophone',
            name='national_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contactphon', to='eCRF.demoinfo'),
        ),
        migrations.AlterField(
            model_name='healthinfo',
            name='national_code',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='health', to='eCRF.demoinfo'),
        ),
    ]
