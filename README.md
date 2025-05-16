# Laporan Proyek Machine Learning - Nama Anda

## Domain Proyek

Pada bagian ini, kamu perlu menuliskan latar belakang yang relevan dengan proyek yang diangkat.

Sektor properti memegang peranan krusial dalam perekonomian suatu wilayah, mencerminkan dinamika sosial dan ekonomi yang kompleks. Di kota Makassar, sebagai salah satu pusat pertumbuhan ekonomi di Sulawesi Selatan, fluktuasi harga rumah menjadi perhatian penting bagi berbagai pihak, sebagaimana tercermin dalam Perkembangan Indeks Harga Konsumen/ Inflasi Kota Makassar Bulan Maret 2021 (BPS Makassar, 2021). Informasi akurat mengenai prediksi harga rumah dapat memberikan manfaat signifikan dalam pengambilan keputusan investasi, perencanaan pembangunan, serta formulasi kebijakan terkait perumahan. Namun, kompleksitas faktor-faktor yang mempengaruhi harga properti, mulai dari karakteristik fisik bangunan, lokasi strategis, hingga kondisi pasar secara keseluruhan, menjadikan prediksi harga rumah sebagai tantangan yang menarik untuk dieksplorasi (Goodfellow et al., 2016). Seiring dengan kemajuan teknologi dan ketersediaan data yang semakin melimpah, pendekatan berbasis machine learning menawarkan potensi yang besar untuk mengembangkan model prediksi yang lebih akurat dan efisien (Jordan & Mitchell, 2015). Beberapa studi telah menunjukkan keberhasilan algoritma seperti Random Forest Regressor dan K-Nearest Neighbors (KNN) dalam memprediksi harga rumah (Rais et al., 2024; Kurniawan et al., 2024). Proyek ini bertujuan untuk mengatasi tantangan tersebut dengan memanfaatkan algoritma Random Forest Regressor, dan K-Nearest Neighbors (KNN) untuk memprediksi harga rumah di kota Makassar, dengan harapan dapat memberikan kontribusi yang berharga bagi pemahaman dan pengambilan keputusan dalam pasar properti lokal.

## Business Understanding

Pada bagian ini, kamu perlu menjelaskan proses klarifikasi masalah.

Bagian laporan ini mencakup:

### Problem Statements

Menjelaskan pernyataan masalah latar belakang:
1. Bagaimana cara memprediksi harga rumah di Kota Makassar secara akurat berdasarkan fitur-fitur seperti lokasi, jumlah kamar tidur dan mandi, luas tanah, luas bangunan, serta ketersediaan carport?
    - Masalah ini timbul karena fluktuasi harga properti yang cukup tinggi, sementara masyarakat dan investor membutuhkan informasi yang akurat untuk pengambilan keputusan.
2. Algoritma machine learning mana yang memberikan performa terbaik dalam memprediksi harga rumah di Kota Makassar?
    - Banyaknya algoritma regresi yang tersedia menimbulkan tantangan dalam memilih model yang paling sesuai dengan karakteristik data lokal Makassar. 
3. Apakah model yang dibangun mampu digunakan untuk melakukan prediksi harga rumah secara konsisten di berbagai rentang harga?
    - Diperlukan validasi untuk memastikan bahwa model tidak hanya akurat di harga rata-rata, tetapi juga pada harga ekstrem (mahal atau murah).

### Goals

Menjelaskan tujuan dari pernyataan masalah:
1. Membangun model prediktif harga rumah berbasis machine learning yang mampu menghasilkan estimasi harga yang mendekati harga sebenarnya dengan error yang minimal.
2. Mengevaluasi dan membandingkan performa tiga algoritma regresi populer yaitu K-Nearest Neighbors (KNN), Random Forest Regressor (RF), dan AdaBoost Regressor dalam konteks pasar properti Makassar.

### Solution statements

1. Mengimplementasikan tiga algoritma machine learning regresi:
    - Menggunakan K-Nearest Neighbors, Random Forest Regressor, dan AdaBoost Regressor sebagai baseline model untuk memprediksi harga rumah.
    - Setiap model akan dievaluasi menggunakan metrik Mean Squared Error (MSE)
2. Melakukan perbandingan performa antar model berdasarkan hasil evaluasi:
    - Memilih model terbaik berdasarkan nilai MSE terendah pada data test.

## Data Understanding

Sumber data berasal dari Scraping data secara mandiri pada website penyedia harga rumah yang saya filter berdasarkan kota Makassar pada situs [berikut](https://www.rumah123.com/jual/makassar/rumah/)

### Variabel-variabel pada Makassar House Price dataset adalah sebagai berikut:
- Title : Judul iklan yang diberikan kepada promotor.
- Lokasi : lokasi rumah yang ditawarkan.
- Jumlah Kamar Tidur : jumlah kamar tidur yang direpresentasikan dalam bentuk integer
- Jumlah Kamar Mandi : jumlah kamar mandi yang direpresentasikan dalam bentuk integer
- Luas Tanah : luas tanah yang direpresentasikan dalam satuan m²
- Luas Bangunan : luas bangunan yang direpresentasikan dalam satuan m²
- Car Port : merepresentasikan atau mengindikasikan tempat parkir beratap terbuka atau semi terbuka
- Price : Harga rumah 
- Timestamp : waktu saat berhasil mendapatkan data dari hasil scraping

### EDA pada Dataset

1. Inaccurate atau anomali pada data


**Rubrik/Kriteria Tambahan (Opsional)**:
- Melakukan beberapa tahapan yang diperlukan untuk memahami data, contohnya teknik visualisasi data atau exploratory data analysis.

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling
Tahapan ini membahas mengenai model machine learning yang digunakan untuk menyelesaikan permasalahan. Anda perlu menjelaskan tahapan dan parameter yang digunakan pada proses pemodelan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan kelebihan dan kekurangan dari setiap algoritma yang digunakan.
- Jika menggunakan satu algoritma pada solution statement, lakukan proses improvement terhadap model dengan hyperparameter tuning. **Jelaskan proses improvement yang dilakukan**.
- Jika menggunakan dua atau lebih algoritma pada solution statement, maka pilih model terbaik sebagai solusi. **Jelaskan mengapa memilih model tersebut sebagai model terbaik**.

## Evaluation
Pada bagian ini anda perlu menyebutkan metrik evaluasi yang digunakan. Lalu anda perlu menjelaskan hasil proyek berdasarkan metrik evaluasi yang digunakan.

Sebagai contoh, Anda memiih kasus klasifikasi dan menggunakan metrik **akurasi, precision, recall, dan F1 score**. Jelaskan mengenai beberapa hal berikut:
- Penjelasan mengenai metrik yang digunakan
- Menjelaskan hasil proyek berdasarkan metrik evaluasi

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.

