import random
from datetime import datetime, timedelta

def generate_transaction_time():
    """
    Menghasilkan datetime acak yang hanya jatuh pada hari kerja (Senin-Sabtu)
    dan dalam jam operasional (08:00 - 18:00).
    """
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2024, 12, 31)

    while True:
        # 1. Hasilkan tanggal acak terlebih dahulu
        time_difference = end_date - start_date
        random_days = random.randint(0, time_difference.days)
        generated_date = start_date + timedelta(days=random_days)

        # 2. Periksa apakah hari tersebut BUKAN hari Minggu (Minggu = 6)
        if generated_date.weekday() != 6:
            break # Jika bukan hari Minggu, lanjutkan

    # 3. Hasilkan waktu acak dalam rentang jam operasional (08:00:00 - 17:59:59)
    start_time_seconds = 8 * 3600  # 8 pagi dalam detik
    end_time_seconds = 18 * 3600 # 6 sore dalam detik
    random_second_in_day = random.randint(start_time_seconds, end_time_seconds - 1)

    # 4. Gabungkan tanggal yang valid dengan waktu yang valid
    transaction_time = generated_date.replace(
        hour=random_second_in_day // 3600,
        minute=(random_second_in_day % 3600) // 60,
        second=random_second_in_day % 60,
        microsecond=0
    )
    
    return transaction_time
