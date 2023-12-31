# Generated by Django 4.0 on 2023-11-18 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', 'initial_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='protocol',
            name='device',
        ),
        migrations.CreateModel(
            name='DeviceProtocol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models_app.device', verbose_name='Устройство')),
                ('protocol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models_app.protocol', verbose_name='Протокол')),
            ],
            options={
                'verbose_name': 'Протокол устройтва',
                'verbose_name_plural': 'Протоколы устройств',
                'db_table': 'device_protocols',
            },
        ),
    ]
