import pandas as pd

from utils.extract import scrape_property
from utils.transform import transform_to_DataFrame, transform_data
from utils.load import convert_to_csv

def main():
    """Fungsi utama keseluruhan proses scraping hingga menyimpannya"""
    BASE_URL = 'https://www.rumah123.com/jual/makassar/makassar/rumah/?itm_medium=search-suggestions-pencarian-terakhir&itm_source=organic&page={}'
    all_property_data = scrape_property(BASE_URL)

    if all_property_data:
        df = transform_to_DataFrame(all_property_data)
        df = transform_data(df)
        print(df)
        print(df.info())

        # menyimpan ke CSV
        convert_to_csv(df)
    else:
        print("Tidak ada data yang ditemukan")

if __name__ == '__main__':
    main()