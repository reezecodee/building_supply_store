from data import structural, roof_ceiling, construction_tools, door_window_sanitary, finishing, plumbing_and_electrical, branch_store, cashier_and_customer
import pandas as pd
import os


data = [
    {
        "name": 'structural_materials',
        "data": structural.structural_items
    },
    {
        "name": 'roof_ceiling_materials',
        "data": roof_ceiling.roof_ceiling_items
    },
    {
        "name": 'construction_tool_materials',
        "data": construction_tools.constructions_tool_items
    },
    {
        "name": 'door_window_sanitary_materials',
        "data": door_window_sanitary.door_window_sanitary_items
    },
    {
        "name": 'finishing_materials',
        "data": finishing.finishing_items
    },
    {
        "name": 'plumbing_and_electrical_materials',
        "data": plumbing_and_electrical.plumbing_and_electrical_items
    },
    {
        "name": "branch_store",
        "data": branch_store.branches
    }   
]

def path(file_name):
    return os.path.join('csv', f"{file_name}.csv")


def createCSVFile(data_list):
    for product_dict in data_list:
        name = product_dict['name']
        product_data = product_dict['data']

        df = pd.DataFrame(product_data)
        df.to_csv(path(name), index=False)
        
        print(f"File '{name}.csv' berhasil dibuat.")
    
    # data cashier
    df_cashier = pd.DataFrame(cashier_and_customer.cashiers)
    df_cashier.to_csv(path('cashiers'), index=False)


createCSVFile(data)