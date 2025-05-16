import pandas as pd
import re

def transform_to_DataFrame(data):
    """Mengubah data menjadi DataFrame."""
    df = pd.DataFrame(data)
    return df

def transform_price(price_str):
    """Mentransform string harga ke dalam bentuk integer satuan rupiah."""
    if isinstance(price_str, (int, float)):
        return int(price_str)
    if not isinstance(price_str, str):
        return None

    price_str = price_str.lower().replace('rp', '').strip()

    try:
        if 'miliar' in price_str:
            value = float(re.search(r'([\d.,]+)\s*miliar', price_str).group(1).replace(',', '.'))
            return int(value * 1_000_000_000)
        elif 'juta' in price_str:
            value = float(re.search(r'([\d.,]+)\s*juta', price_str).group(1).replace(',', '.'))
            return int(value * 1_000_000)
        elif 'ribu' in price_str:
            value = float(re.search(r'([\d.,]+)\s*ribu', price_str).group(1).replace(',', '.'))
            return int(value * 1_000)
        else:
            # Jika tanpa satuan, bersihkan pemisah dan konversi langsung
            price_value_str = price_str.replace('.', '').replace(',', '.')
            return int(float(price_value_str))
    except (AttributeError, ValueError):
        return None

def transform_data(data):
    """Menggabungkan semua transformasi data menjadi satu fungsi"""

    # Transform price
    data['Price'] = data['Price'].apply(transform_price)

    # Transform Luas Tanah
    data['Luas Tanah'].replace(' m²', '', regex=True, inplace=True)
    data.dropna(subset=['Luas Tanah'], inplace=True)
    data['Luas Tanah'] = data['Luas Tanah'].astype(int)

    # Transform Luas Bangunan
    data['Luas Bangunan'].replace(' m²', '', regex=True, inplace=True)
    data.dropna(subset=['Luas Bangunan'], inplace=True)
    data['Luas Bangunan'] = data['Luas Bangunan'].astype(int)

    # Transform lokasi
    data['Lokasi'] = data['Lokasi'].replace(', Makassar', '', regex=True)

    # Transform Car Port
    data['Car Port'] = data['Car Port'].fillna(0)

    # Transform Kamar Tidur dan Mandi
    data.dropna(subset=['Jumlah Kamar Tidur'], inplace=True)
    data.dropna(subset=['Jumlah Kamar Mandi'], inplace=True)
    



    return data



