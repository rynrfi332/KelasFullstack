
# Langkah 1: Impor pustaka yang diperlukan
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Langkah 1: Baca file Excel
df_urls = pd.read_excel('Book1.xlsx', usecols=['A'])

# Langkah 2: Ambil daftar URL dari kolom A
urls = df_urls['A'].tolist()

# Langkah 3: Loop melalui daftar URL dan ekstrak data
for url in urls:
    response = requests.get(url)

    # Langkah 4: Parse konten HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Langkah 5: Cari semua elemen <h1> dan ekstrak teksnya
    h1_tags = soup.find_all('h1')
    h1_texts = [tag.text.strip() for tag in h1_tags]

    # Langkah 6: Buat DataFrame dari list elemen <h1>
    df = pd.DataFrame(h1_texts, columns=['H1 Text'])

    # Langkah 7: Simpan DataFrame ke dalam file Excel
    excel_filename = f'h1_tags_{url}.xlsx'  # Nama file Excel sesuai dengan URL website
    df.to_excel(excel_filename, index=False)

    print(f'Data dari {url} berhasil disimpan ke {excel_filename}')
    response = requests.get(url)

    # Langkah 3: Parse konten HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Langkah 4 & 5: Cari semua elemen <h1> dan ekstrak teksnya
    h1_tags = soup.find_all('h1')
    h1_texts = [tag.text.strip() for tag in h1_tags]

    # Langkah 6: Buat DataFrame dari list elemen <h1>
    df = pd.DataFrame(h1_texts, columns=['H1 Text'])

    # Langkah 7: Simpan DataFrame ke dalam file Excel
    excel_filename = f'h1_tags_{url}.xlsx'  # Nama file Excel sesuai dengan URL website
    df.to_excel(excel_filename, index=False)

    print(f'Data dari {url} berhasil disimpan ke {excel_filename}')
