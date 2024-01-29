import joblib
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# Judul aplikasi
st.title('Klasifikasi Kelulusan Mahasiswa TI UNTIRTA')

# Masukkin gambar
st.subheader('Keterangan Nilai Bobot Mata Kuliah')
img = Image.open('Nilai Bobot Mata Kuliah.jpg')
st.image(img, use_column_width = True)

# Masukkan Nama
Nama_Lengkap = st.text_input("Nama Lengkap: ")

# Masukkan NIM
NIM = st.number_input("NIM:", min_value=0, max_value=3333999999, value=0)

# Set st.session_state setelah pengguna memasukkan Nama dan NIM
if Nama_Lengkap:
    st.session_state.name = Nama_Lengkap

if NIM:
    st.session_state.age = NIM

SEMESTER_1 = joblib.load('MODEL_SEMESTER1_RF.pkl')

# Sidebar for navigation

with st.sidebar:
    selected = option_menu('Klasifikasi Kelulusan Mahasiswa Teknik Industri UNTIRTA',
                           ['SEMESTER 1', 'SEMESTER 2', 'SEMESTER 3', 'SEMESTER 4',
                            'SEMESTER 5', 'SEMESTER 6', 'SEMESTER 7'],
                           default_index=0)

# Diabetes Prediction Page
if (selected == 'SEMESTER 1'):

    # Page title
    st.title('Klasifikasi Kelulusan Mahasiswa Semester 1 Teknik Industri UNTIRTA')

    Fisika_Dasar_1 = st.selectbox('Fisika Dasar 1', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kalkulus_1 = st.selectbox('Kalkulus 1', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kimia_Dasar = st.selectbox('Kimia Dasar', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Material_Teknik = st.selectbox('Material Teknik', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Pengantar_Teknik_Industri = st.selectbox('Pengantar Teknik Industri', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Menggambar_Teknik = st.selectbox('Menggambar Teknik', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Menggambar_Teknik = st.selectbox('Praktikum Menggambar Teknik', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Logika_Pemrograman = st.selectbox('Logika Pemrograman', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))

    # Code for prediction
    SEMESTER_1_PREDICTION = ''

    # Creating a button for prediction

    if st.button('KLASIFIKASI KELULUSAN'):
        if 'name' in st.session_state:
            st.write(f"Halo {st.session_state.name}!")

        if 'age' in st.session_state:
            st.write(f"NIM {st.session_state.age}.")

        Fisika_Dasar_1 = float(Fisika_Dasar_1)
        Kalkulus_1 = float(Kalkulus_1)
        Kimia_Dasar = float(Kimia_Dasar)
        Material_Teknik = float(Material_Teknik)
        Pengantar_Teknik_Industri = float(Pengantar_Teknik_Industri)
        Menggambar_Teknik = float(Menggambar_Teknik)
        Praktikum_Menggambar_Teknik = float(Praktikum_Menggambar_Teknik)
        Logika_Pemrograman = float(Logika_Pemrograman)

        SEMESTER_1_prediction = SEMESTER_1.predict([[Fisika_Dasar_1, Kalkulus_1, Kimia_Dasar, Material_Teknik, Pengantar_Teknik_Industri, Menggambar_Teknik, Praktikum_Menggambar_Teknik, Logika_Pemrograman]])

        if SEMESTER_1_prediction[0] == 1:
            SEMESTER_1_PREDICTION = 'KAMU TERMASUK KLASIFIKASI MAHASISWA LULUS TIDAK TEPAT WAKTU!'
            MOTIVASI = (
                ' Jangan patah semangat, terus perbaiki nilaimu. Ini baru semester 1 dan harus cepat beradaptasi. '
                'Jika kamu malas dan hanya membuang-buang waktu, kamu tak akan tahu bagaimana cara merengkuh peluang bahkan ketika peluang itu tepat berada di hadapan kamu.')
            img3 = Image.open('SYARAT NILAI.jpg')
            st.image(img3, use_column_width=True)

        else:
            SEMESTER_1_PREDICTION = 'SELAMAT KAMU TERMASUK KLASIFIKASI LULUS TEPAT WAKTU!'
            MOTIVASI = (
                ' Kamu telah melalui lebih dari 20 sks dengan baik. Pertahankan dan tingkatkan kembali nilai-nilai di semester kedepan. '
                'Kamu bisa mengambil lebih dari 20 sks untuk semester 2. Tidak apa-apa untuk merayakan kesuksesan, tapi lebih penting untuk memperhatikan pelajaran tentang kegagalan.')

        pesan_hasil = f'{SEMESTER_1_PREDICTION}, {MOTIVASI}'

        st.success(pesan_hasil)
