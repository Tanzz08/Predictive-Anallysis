import requests 
import pandas as pd
from bs4 import BeautifulSoup
import time 
from datetime import datetime
import re

# user-agent
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        "(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    )
}

def fetching_content(url):
    """Mengambil konten HTML dari url yang diberikan"""
    session = requests.Session()
    response = session.get(url, headers=HEADERS)
    try:
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Terjadi kesalahan ketika melakukan requests terhadap {url}: {e}")
        return None

def extract_property_data(card):
    """Ekstrak data rumah dari satu elemen card"""

    # # Harga
    # price_tag = card.find(lambda tag: tag.name in ['div', 'span'] and 'Rp' in tag.text)
    # price = price_tag.text.strip() if price_tag else None

    price_parent = card.find('div', class_='card-featured__middle-section__price')
    price = price_parent.find('strong').text

    # Title (judul iklan rumah)
    title_tag = card.find('a') # Mengambil tag a untuk title
    title = title_tag.text.strip() if title_tag else None

    # Lokasi
    lokasi = None
    lokasi_parent = card.find('div', class_='card-featured__middle-section')
    if lokasi_parent:
        lokasi_spans = lokasi_parent.find_all('span')
        for span in lokasi_spans:
            if span.text.strip().endswith(", Makassar"):
                lokasi = span.text.strip()
                break  # Asumsi kita hanya perlu satu lokasi yang sesuai
            elif ", Makassar" in span.text:
                # Sebagai fallback, jika ada ", Makassar" di tengah, kita ambil juga
                lokasi = span.text.strip()
                break


    # Jumlah kamar tidur dan kamar mandi (berurutan)
    attributes = card.find_all('span', class_='attribute-text')
    jumlah_kamar = attributes[0].text.strip() if len(attributes) > 0 else None
    jumlah_kamar_mandi = attributes[1].text.strip() if len(attributes) > 1 else None
    carport = attributes[2].text.strip() if len(attributes) > 2 else None

    # Ambil semua div.attribute-info
    attribute_divs = card.find_all("div", class_="attribute-info")
    lt = attribute_divs[0].find("span").text.strip() if len(attribute_divs) > 0 else None
    lb = attribute_divs[1].find("span").text.strip() if len(attribute_divs) > 1 else None

    return {
        "Title": title,
        "Lokasi": lokasi,
        "Jumlah Kamar Tidur": jumlah_kamar,
        "Jumlah Kamar Mandi": jumlah_kamar_mandi,
        "Luas Tanah": lt,
        "Luas Bangunan": lb,
        "Car Port": carport,
        "Price": price,
        "Timestamp": datetime.now()
    }

def scrape_property(base_url, start_page=1, delay=2):
    """Scrape seluruh properti dari halaman dengan pagination"""
    data = []
    page_number = start_page

    while True:
        if page_number == 1:
            url = base_url.format("")
        else:
            url = base_url.format(f"{page_number}")

        print(f"Scraping halaman: {url}")
        content = fetching_content(url)
        if content:
            soup = BeautifulSoup(content, "html.parser")
            cards = soup.find_all('div', class_='featured-card-component')

            for card in cards:
                property_data = extract_property_data(card)
                data.append(property_data)

            # Cek apakah tombol "Next" tersedia
            next_li = soup.find("li", class_="ui-molecule-paginate__item--next")
            next_link = next_li.find("a") if next_li else None

            if next_link and next_link.get("aria-disabled") != "true":
                page_number += 1
                time.sleep(delay)
            else:
                break
        else:
            break

    return data
