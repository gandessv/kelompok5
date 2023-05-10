import streamlit as st
from streamlit_option_menu import option_menu

# navigasi
with st.sidebar :
    
    selected = option_menu ('clickclock',
                            ['Home',
                             'Definisi',
                             'Hitung Konsentrasi Terukur',
                             'Hitung Kadar',
                             'Hitung %RSD'],
                            default_index=0)
    
# pengertian
if (selected == 'Home') :
    
    st.header("Aplikasi Project Logika dan Pemprograman Komputer")
    st.markdown('''Kelompok 5:
1. Amanda Berliana Widjaya (2260005)
2. Fifi Nuraini (2260016)
3. Marlina Cahyani (2260027)
4. Putri Nuraini (2260038)
5. Ruri Dwi Arlita (2260049)
6. Afdatul Saputra (2120377)''')

# halaman definisi
if (selected == 'Definisi') :
    st.title('DEFINISI')
    st.header('Konsentrasi Terukur')
    st.markdown("""Konsentrasi analit yang terukur merupakan penentuan konsentrasi analit dalam sampel secara kuantitatif dengan menggunakan instrumentasi kimia secara umum dapat dilakukan melalui kurva kalibrasi yang memiliki linearitas yang memenuhi batas keberterimaan. Kurva kalibrasi merupakan grafik yang membentuk garis lurus (linear) yang menyatakan hubungan antara konsentrasi larutan kerja termasuk blanko dengan respons yang proporsional dari instrumen yang digunakan""")

    st.header('Kadar')
    st.markdown("""Zat yang ditetapkan disebut konstituen yang diinginkan atau analit. Sedangkan jumlah banyaknya suatu zat tertentu dalam sampel biasanya dinyatakan sebagai kadar atau konsentrasi, misalnya persen berat, molar, gram per liter, atau ppm.""")
    
    st.header('%RSD')
    st.markdown("""Dalam teori probabilitas dan statistik, standar deviasi relatif (RSD atau %RSD) adalah nilai absolut dari koefisien variasi. 

Deviasi standar relatif, yang juga dapat disebut sebagai RSD atau koefisien variasi, digunakan untuk menentukan apakah standar deviasi dari sekumpulan data kecil atau besar bila dibandingkan dengan rata-rata.

Menurut Christian (1994) nilai RSD yang baik adalah < 5% untuk tingkat kepercayaan 95%. Berdasarkan nilai RSD yang didapat maka metode tergolong baik. Akurasi merupakan ukuran yang menunjukkan derajat kedekatan hasil analisis dengan konsentrasi analit yang sebenarnya""")
    
# halaman cterukur
if (selected == 'Hitung Konsentrasi Terukur') :
    st.title('KONSENTRASI TERUKUR')
    
    st.write("perhitungan mencari konsentrasi terukur")
    st.latex(r''' (absorbansi-intersep)/slope ''')
    absorbansi = st.number_input ("masukkan absorbansi")
    intersep = st.number_input ("masukkan nilai intercep")
    slope = st.number_input ("masukkan nilai slope")
    hitung = st.button ("hitung konsentrasi terukur")
    
    if hitung :
        konsentrasi_terukur = (absorbansi - intersep) / slope
        st.write ("nilai konsentrasi terukur adalah = mg/L ")
        st.success (f"nilai konsentrasi terukur adalah = {konsentrasi_terukur} mg/L ")
        
# hitung kadar
if (selected == 'Hitung Kadar') :
    st.title('KADAR')
    st.write("perhitungan mencari kadar pada sampel")
    st.latex(r''' (Cterukur * VLT * fp) / sampel ''')
    cterukur = st.number_input ("Masukkan Nilai Konsentrasi Terukur")
    vlt = st.number_input ("Masukkan Nilai Volume Labu Takar")
    fp = st.number_input ("Masukkan Nilai fp")
    sampel = st.number_input ("Masukkan Nilai Volume atau berat sampel")
    st.write("#Keterangan : sampel yang dimasukkan dapat berupa bobot ataupun volume") 
    button = st.button ("hitung kadar")
    
    if button :
        kadar = (cterukur*vlt*fp) / sampel
        st.write ("nilai kadar adalah = ")
        st.success (f"nilai konsentrasi terukur adalah = {kadar} ")
        
        
# hitung %RSD
if (selected == 'Hitung %RSD') :
    st.title('%RSD')
    
    nilai_total_kadar = st.number_input ("masukkan nilai total kadar")
    banyak_jumlah_kadar = st.number_input ("masukkan banyak data kadar")
    
    hitung = st.button('Hitung Nilai %RSD')
    
    if hitung :
        RSD = (nilai_total_kadar**1/2)/(nilai_total_kadar/banyak_jumlah_kadar)
        st.write ("nilai %RSD adalah = ")
        st.success (f"nilai %RSD adalah = {RSD} %")