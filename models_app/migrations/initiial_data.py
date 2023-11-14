import os
import pandas as pd

from django.db import migrations

from models_app.models import *


def added_registry(registry, initial_data):
    initial_data_last_key = list(initial_data.keys())[-1]
    if isinstance(initial_data[initial_data_last_key], list):
        if not isinstance(registry, float):
            initial_data[initial_data_last_key].append(registry)
    else:
        type_of_registry_last_key = list(initial_data[initial_data_last_key])[-1]
        if not isinstance(registry, float):
            initial_data[initial_data_last_key][type_of_registry_last_key].append(registry)


def initial_data_migration(first_param, second_param):
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'registry.xlsx')
    df = pd.read_excel(file_path)
    initial_data = {}
    for column in df.columns:
        column_values = df[column]
        if 'Unnamed' not in column and column not in initial_data:
            initial_data[column] = []
            for index, value in enumerate(column_values):
                if not isinstance(value, float) and index == 0:
                    initial_data[column] = {value: []}
                else:
                    added_registry(value, initial_data)
        else:
            initial_data_last_key = list(initial_data.keys())[-1]
            for index, value in enumerate(column_values):
                if not isinstance(value, float) and index == 0:
                    initial_data[initial_data_last_key][value] = []
                else:
                    added_registry(value, initial_data)
    for key in initial_data.keys():
        device = Device.objects.create(name=key)
        if isinstance(initial_data[key], list):
            registry_obj_list = []
            for number in initial_data[key]:
                registry_obj_list.append(
                    RegistryNumber(number=number, device=device)
                )
            RegistryNumber.objects.bulk_create(registry_obj_list)
        else:
            for name in initial_data[key].keys():
                type = Type.objects.create(name=name)
                device.type.add(type)
                registry_obj_list = []
                for number in initial_data[key][name]:
                    registry_obj_list.append(
                        RegistryNumber(number=number, device=device)
                    )
                RegistryNumber.objects.bulk_create(registry_obj_list)



class Migration(migrations.Migration):
    dependencies = [
        ('models_app', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(initial_data_migration),
    ]