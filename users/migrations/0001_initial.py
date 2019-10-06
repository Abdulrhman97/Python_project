# Generated by Django 2.2.5 on 2019-09-25 07:18

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics ')),
                ('city', models.CharField(choices=[('riyadh', 'Riyadh Province -  الرياض'), ('jeddah', 'Jeddah Province -  جدة'), ('medinah', 'Medinah Province -  المدينة'), ('makkah', 'Makkah Province - مكة'), ('qassim', 'Qassim Province - القصيم'), ('easter', 'Easter Province - المنطقه الشرقيه'), ('asir', 'Asir Province -  عسير'), ('tabuk', 'Tabuk Province -  تبوك'), ('hail', 'Hail Province -  حايل'), ('northern', 'Norther Borders -  منطقة الحدود الشماليه'), ('jizan', 'Jizan Province -  جيزان'), ('tabuk', 'Tabuk Province -  تبوك'), ('bahah', 'Bahah Province -  الباحة'), ('najran', 'Najran Province -  نجران')], default='riyadh', max_length=20, null=True)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
