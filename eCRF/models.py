from django.db import models
from django_countries.fields import CountryField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.shortcuts import reverse


class DemoInfo(models.Model):
    GENDER = [
        ('wom', 'زن'),
        ('man', 'مرد'),
        ('ukw', 'نامشخص'),
    ]
    EDUCATE_RATE = [
        ('illit', 'بی سواد'),
        ('elmnt', 'ابتدایی'),
        ('dplom', 'دیپلم'),
        ('tchnc', 'کاردانی'),
        ('exprt', 'کارشناسی'),
        ('Mstrs', 'کارشناسی ارشد'),
        ('Phd', 'دکتری'),
    ]
    ECONOMIC_SITUATION = [
        ('low', 'ضعیف'),
        ('norm', 'متوسط'),
        ('good', 'خوب'),
        ('best', 'عالی'),
    ]
    STATUS_JOB = [
        ('1', 'موضوعیت ندارد'),
        ('2', 'بیکار'),
        ('3', 'کشاورز'),
        ('4', 'کارگر'),
        ('5', 'کارمند'),
        ('6', 'بازنشسته'),
        ('7', 'آزاد'),
    ]
    national_code = models.CharField(max_length=10)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    birthday = models.DateField()
    gender = models.CharField(max_length=8, choices=GENDER)
    educate_rate = models.CharField(max_length=10, choices=EDUCATE_RATE)
    economic_situation = models.CharField(max_length=10, choices=ECONOMIC_SITUATION)
    status_job = models.CharField(max_length=20, choices=STATUS_JOB)
    country = CountryField()
    datetime_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    datetime_modified = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.national_code

    def get_absolute_url(self):
        return reverse('patient_detail', args=[self.pk])


class HealthInfo(models.Model):
    national_code = models.ForeignKey(DemoInfo, on_delete=models.CASCADE, default=1234567890, related_name='health',
                                      blank=True)
    age = models.PositiveIntegerField(validators=[MinValueValidator(5), MaxValueValidator(130)])
    weight = models.DecimalField(max_length=4, max_digits=4, decimal_places=1, validators=[MinValueValidator(10),
                                                                                           MaxValueValidator(400)])
    height = models.DecimalField(max_length=4, max_digits=4, decimal_places=1, validators=[MinValueValidator(70),
                                                                                           MaxValueValidator(250)])
    BMI = models.DecimalField(max_length=3, max_digits=3, decimal_places=1, validators=[MinValueValidator(10),
                                                                                        MaxValueValidator(50)])
    pregnancy_status = models.BooleanField(default=False)
    breast_feeding_status = models.BooleanField(default=False)
    smoking = models.BooleanField(default=False)


    # def get_absolute_url(self):
    #     return reverse('patient_detail', args=[self.national_code])


class ContactInfoAddress(models.Model):
    national_code = models.ForeignKey(DemoInfo, on_delete=models.CASCADE, default=1234567890, related_name='contactadd')
    country = CountryField()
    province = models.CharField(max_length=15)
    town = models.CharField(max_length=15)
    village = models.CharField(max_length=15)
    post_code = models.CharField(max_length=10)


class ContactInfoPhone(models.Model):
    national_code = models.ForeignKey(DemoInfo, on_delete=models.CASCADE, default=1234567890, related_name='contactphon')
    home_phone = models.CharField(max_length=11)
    cell_phone = models.CharField(max_length=11)
    fax = models.CharField(max_length=11)
    work_phone = models.CharField(max_length=11)
    cellular_phone = models.CharField(max_length=11)
    health_care_proxy_phone = models.CharField(max_length=11)
    emergency_phone = models.CharField(max_length=11)

