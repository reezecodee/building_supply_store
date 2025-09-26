import os
import pandas as pd

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

    df_product = pd.DataFrame(master_product_list)
    df_product.to_csv('price_list.csv', index=False)