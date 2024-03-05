import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# membaca data
df = pd.read_csv("https://raw.githubusercontent.com/prazka/BikeAnalysis/main/Final_Data_Bike.csv")

st.title('Analisis Data Sepeda')
tab1, tab2, tab3 = st.tabs(["Overview", "Pertanyaan 1", "Pertanyaan 2"])
 
with tab1:
    st.header("Overview")
    st.markdown("#### Dashboard Sederhana dari dataset Bike")
    st.text("# Proyek Analisis Data: [Input Nama Dataset]")
    st.text("- Nama: [Prazka Aldiyuda]")
    st.text("- Email: [m295d4ky2383@bangkit.academy]")
    st.text("- ID Dicoding: [prazka]")
    st.text("""Menentukan Pertanyaan Bisnis

    Terdapat dua buah pertanyaan yang akan dijawab pada tab selanjutnya yaitu :
    1.   Apa pengaruh cuaca terhadap peminjaman sepeda?
    2.   Apa pengaruh hari terhadap peminjaman sepeda?""")
    
    
 
with tab2:
    df1=df.copy()
    st.header("Pertanyaan 1")
    st.markdown("#### Apa pengaruh cuaca terhadap peminjaman sepeda?")
    # Membuat variabel map untuk mengubah menjadi deskriptif
    df1['weathersit'] = df1['weathersit'].map({1: 'Cerah', 2: 'Mendung', 3: 'Hujan Ringan', 4: 'Hujan Lebat'})

    # Mengatur urutan kelas
    weathersit_order = ['Cerah', 'Mendung', 'Hujan Ringan', 'Hujan Lebat']

    # Membuat pivot tabel untuk rata-rata jumlah peminjaman sepeda terhadap variabel cuaca dan musim
    pivot_weathersit = df1.groupby(by=["weathersit"]).agg({
    "cnt": "median"
    }).reindex(weathersit_order, fill_value=0).reset_index()

    # Menampilkan pivot tabel
    pd.options.display.float_format = '{:.2f}'.format
    st.text("Median jumlah peminjaman sepeda terhadap keadaan cuaca :")
    st.text(pivot_weathersit.to_string(index=False))

    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))

    sns.countplot(x='weathersit', data=df1)
    plt.title('Distribusi Data berdasarkan cuaca')
    plt.xlabel('Cuaca')
    plt.ylabel('Jumlah pengguna')

    st.pyplot()

    sns.boxplot(x="weathersit", y="cnt", data=df1)
    plt.title("Distribusi pengguna berdasarkan cuaca")
    plt.xlabel('Cuaca')
    plt.ylabel('Jumlah pengguna')
    st.pyplot()

    st.markdown("### Kesimpulan")
    st.text("""Cuaca sangat mempengaruhi jumlah sepeda yang digunakan
    dimana bisa dilihat pada sebaran data pada saat kondisi cuaca cerah 
    sangat banyak sekali yang meminjam sepeda dibandingkan saat berawan, 
    hujan ringan maupun lebat. Hal ini juga didukung oleh perhitungan median 
    dimana didapati nilai dari media peminjaman sepeda atau CNT pada saat 
    cuaca cerah adalah 159, sedangkan ketika mendung senilai 133 selain itu 
    ketika hujan ringan adalah Hujan Ringan 63.00 dan terakhir Hujan Lebat 
    senilai 36.00 alasan perhitungan median karena banyak sekali outlier dalam 
    data yang digunakan.""")

    
 
with tab3:
    df2= df.copy()
    st.header("Pertanyaan 2")
    st.markdown("### Apa pengaruh hari terhadap peminjaman sepeda?")

    pivot_weekday = df2.groupby(by=["weekday"]).agg({
    "cnt": "median"
    }).reindex(['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']).reset_index()

    st.text("Median jumlah peminjaman sepeda terhadap hari :")
    st.text(pivot_weekday.to_string(index=False))

    sns.boxplot(x="weekday", y="cnt", data=df2,order=['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'])
    plt.title("Distribusi `cnt` berdasarkan `Hari`")
    plt.xlabel('Hari')
    plt.ylabel('Jumlah Pengguna')
    st.pyplot()

    st.markdown("### Kesimpulan")
    st.text("""terjadi tren pola dimana jumlah pengguna meningkat dari hari senin
     menuju hari jumat dan terjadi penurunan pada hari sabtu dan minggu hal ini bisa
      dilihat pada hasil median setiap harinya. Dimana data hari senin berada pada nilai 132 dan pada hari jumat
      senilai 158. Alasan penggunaan median adalah karena 
      banyaknya outlier yang dapat mempengaruhi perhitungan. """)
