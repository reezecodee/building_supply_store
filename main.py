import pandas as pd
import numpy as np
import random
import os 
from data.cashier_and_customer import random_cashier_name, random_customer_name
from generate_datetime import generate_transaction_time

print("Memulai proses pembuatan dataset riwayat transaksi...")

file_names = [
    "construction_tool_materials.csv",
    "door_window_sanitary_materials.csv",
    "finishing_materials.csv",
    "plumbing_and_electrical_materials.csv",
    "roof_ceiling_materials.csv",
    "structural_materials.csv"
]
# Menggabungkan nama folder 'csv' dengan setiap nama file
product_files = [os.path.join('csv', fname) for fname in file_names]

all_products_dfs = []
print("Membaca file-file produk dari folder 'csv'...")
for f_path in product_files:
    try:
        df = pd.read_csv(f_path)
        all_products_dfs.append(df)
        print(f" - Berhasil memuat {f_path}")
    except FileNotFoundError:
        print(f" - PERINGATAN: File {f_path} tidak ditemukan. Dilewati.")

if not all_products_dfs:
    print("\nERROR: Tidak ada file produk yang berhasil dimuat. Proses dihentikan.")
else:
    master_product_list = pd.concat(all_products_dfs, ignore_index=True)
    if 'product' in master_product_list.columns:
        master_product_list.rename(columns={'product': 'product_name'}, inplace=True)
    print("Berhasil menggabungkan semua data produk.")

    # --- 2. Memuat Data Cabang Toko ---
    branch_file_path = os.path.join('csv', 'branch_store.csv')
    try:
        branch_df = pd.read_csv(branch_file_path)
        print(f"Berhasil memuat data cabang toko dari {branch_file_path}.")
    except FileNotFoundError:
        print(f"PERINGATAN: {branch_file_path} tidak ditemukan. Menggunakan data default.")
        branch_df = pd.DataFrame({
            'store_location': ['Jakarta', 'Bandung', 'Surabaya'],
            'type_store': ['Branch', 'Branch', 'Branch']
        })

    # --- 3. Proses Pembuatan Data Transaksi ---
    print("Membuat data transaksi...")

    num_transactions = 30000
    transaction_history = []

    for i in range(num_transactions):
        product_sample = master_product_list.sample(1).iloc[0]
        store_sample = branch_df.sample(1).iloc[0]
        unit_purchase = random.randint(1, 50)
        price_per_unit = pd.to_numeric(product_sample['price_per_unit'], errors='coerce')
        price_per_unit = price_per_unit if pd.notna(price_per_unit) else 0
        total_price = unit_purchase * price_per_unit
        transaction = {
            'product_name': product_sample['product_name'],
            'brand': product_sample.get('brand', np.nan),
            'product_type': product_sample.get('product_type', np.nan),
            'unit': product_sample.get('unit', np.nan),
            'unit_purchase': unit_purchase,
            'price_per_unit': price_per_unit,
            'total_price': total_price,
            'currency': product_sample.get('currency', 'IDR'),
            'date': generate_transaction_time(),
            'delivery': random.choice(['Pickup', 'Delivery']),
            'store_location': store_sample['store_location'],
            'type_store': store_sample['type_store'],
            'customer_name': random_customer_name(random.choice(["random", "male", "female"])),
            'cashier_name': random_cashier_name(store_sample['store_location'])
        }
        transaction_history.append(transaction)

    transactions_df = pd.DataFrame(transaction_history)
    final_columns = [
        'product_name', 'brand', 'product_type', 'unit', 'unit_purchase',
        'price_per_unit', 'total_price', 'currency', 'date', 'delivery',
        'store_location', 'type_store', 'customer_name', 'cashier_name'
    ]
    transactions_df = transactions_df[final_columns]

    # --- 4. Menyimpan Hasil ---
    output_filename = "building_supply_store_sales_2020-2024.csv"
    path = os.path.join('csv', output_filename)
    transactions_df.to_csv(path, index=False)
    print(f"\nBERHASIL! Sebanyak {len(transactions_df)} data transaksi telah dibuat.")
    print(f"File disimpan sebagai: {output_filename}")