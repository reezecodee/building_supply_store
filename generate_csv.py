from data import structural, roof_ceiling, construction_tools, door_window_sanitary, finishing, plumbing_and_electrical
import pandas as pd
import os


data = [
    {
        "name": 'structural',
        "data": structural.structural_items
    },
    {
        "name": 'roof_ceiling',
        "data": roof_ceiling.roof_ceiling_items
    },
    {
        "name": 'construction_tool',
        "data": construction_tools.constructions_tool_items
    },
    {
        "name": 'door_window_sanitary',
        "data": door_window_sanitary.door_window_sanitary_items
    },
    {
        "name": 'finishing',
        "data": finishing.finishing_items
    },
    {
        "name": 'plumbing_and_electrical',
        "data": plumbing_and_electrical.plumbing_and_electrical_items
    }
]


def createCSVFile(data_list):
    for product_dict in data_list:
        name = product_dict['name']
        product_data = product_dict['data']

        df = pd.DataFrame(product_data)
        
        path = os.path.join('csv', f"{name}_materials.csv")
        df.to_csv(path, index=False)
        
        print(f"File '{name}_materials.csv' berhasil dibuat.")


createCSVFile(data)