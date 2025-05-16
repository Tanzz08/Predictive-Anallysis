from sqlalchemy import create_engine
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import pandas as pd

def convert_to_csv(df):
    """Fungsi untuk mengubah dataframe ke CSV"""
    df.to_csv('housePrice_makassar_from_rumah123.csv', index=False)

