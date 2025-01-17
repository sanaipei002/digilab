# Generated by Django 5.1.3 on 2024-12-10 07:02

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labpersonnel', '0001_initial'),
        ('patients', '0002_alter_patient_first_name_alter_patient_last_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestAvailable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AlterField(
            model_name='labpersonnel',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='labpersonnel',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='BroadcastedRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('broadcasted_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('lab_personnel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labpersonnel.labpersonnel')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_requested', models.DecimalField(decimal_places=2, max_digits=10)),
                ('requested_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_paid', models.BooleanField(default=False)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labpersonnel.testavailable')),
            ],
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.TextField()),
                ('date_performed', models.DateTimeField(auto_now_add=True)),
                ('date_reported', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
                ('performed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labpersonnel.labpersonnel')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labpersonnel.testavailable')),
            ],
        ),
    ]
