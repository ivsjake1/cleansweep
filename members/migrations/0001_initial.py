# Generated by Django 4.0.3 on 2023-05-27 16:00

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
            name='ProfileInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(blank=True, default=18, null=True)),
                ('contact_number', models.CharField(blank=True, default='00000000000', max_length=11, null=True)),
                ('city', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('barangay', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('street', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('building', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('house_no', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
