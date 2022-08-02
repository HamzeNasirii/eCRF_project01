# Generated by Django 4.0.2 on 2022-08-02 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eCRF', '0005_alter_healthinfo_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='demoinfo',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='demoinfo',
            name='datetime_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='contactinfoaddress',
            name='national_code',
            field=models.ForeignKey(default=1234567890, on_delete=django.db.models.deletion.CASCADE, related_name='contactadd', to='eCRF.demoinfo'),
        ),
        migrations.AlterField(
            model_name='contactinfophone',
            name='national_code',
            field=models.ForeignKey(default=1234567890, on_delete=django.db.models.deletion.CASCADE, related_name='contactphon', to='eCRF.demoinfo'),
        ),
        migrations.AlterField(
            model_name='demoinfo',
            name='economic_situation',
            field=models.CharField(choices=[('low', 'ضعیف'), ('norm', 'متوسط'), ('good', 'خوب'), ('best', 'عالی')], max_length=10),
        ),
        migrations.AlterField(
            model_name='demoinfo',
            name='educate_rate',
            field=models.CharField(choices=[('illit', 'بی سواد'), ('elmnt', 'ابتدایی'), ('dplom', 'دیپلم'), ('tchnc', 'کاردانی'), ('exprt', 'کارشناسی'), ('Mstrs', 'کارشناسی ارشد'), ('Phd', 'دکتری')], max_length=10),
        ),
        migrations.AlterField(
            model_name='demoinfo',
            name='gender',
            field=models.CharField(choices=[('wom', 'زن'), ('man', 'مرد'), ('ukw', 'نامشخص')], max_length=8),
        ),
        migrations.AlterField(
            model_name='demoinfo',
            name='status_job',
            field=models.CharField(choices=[('1', 'موضوعیت ندارد'), ('2', 'بیکار'), ('3', 'کشاورز'), ('4', 'کارگر'), ('5', 'کارمند'), ('6', 'بازنشسته'), ('7', 'آزاد')], max_length=20),
        ),
        migrations.AlterField(
            model_name='healthinfo',
            name='national_code',
            field=models.ForeignKey(blank=True, default=1234567890, on_delete=django.db.models.deletion.CASCADE, related_name='health', to='eCRF.demoinfo'),
        ),
    ]
