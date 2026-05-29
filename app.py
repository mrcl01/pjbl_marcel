import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="matematika geometri"
)

with st.sidebar:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("logo.png")
        st.title("bagun datar")
        pilihan = st.selectbox("pilih bangun datar", ["persegi", "persegi panjang", "lingkaran", "segitiga", "jajar genjang"])
        st.caption("dibuat dengan :fire: oleh **Marcellino**")

match pilihan:
    case "persegi":
        st.title("persegi")
        st.markdown("menghitung 'luas' dan 'keliling' persegi")
        sisi = st.number_input("masukkan sisi", 0)
        if st.button("hitung", type="primary"):
            luas = sisi * sisi
            keliling = 4 * sisi
            st.success(f"luas persegi adalah: {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            st.balloons()


    case "persegi panjang":
        st.title("persegi panjang")
        st.markdown("menghitung 'luas' dan 'keliling' persegi panjang")
        panjang = st.number_input("masukkan nilai panjang",0)
        lebar = st.number_input("masukkan nilai lebar",0)
        if st.button("hitung", type="primary"):
            luas = panjang * lebar
            keliling = 2 * (panjang + lebar)
            st.success(f"luas persegi panjang adalah: {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            st.balloons()

    case "lingkaran":
        st.title("lingkaran")
        st.markdown("menghitung 'luas' dan 'keliling' lingkaran")
        jari_jari = st.number_input("masukkan nilai jari-jari",0)
        if st.button("hitung", type="primary"):
            luas = 3.14 * (jari_jari ** 2)
            keliling = 2 * 3.14 * jari_jari
            st.success(f"luas lingkaran adalah: {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            st.balloons()

    case "segitiga":
        st.title("segitiga")
        st.markdown("menghitung 'luas' dan 'keliling' segitiga")
        alas = st.number_input("masukkan nilai alas",0)
        tinggi = st.number_input("masukkan nilai tinggi",0)
        sisi1 = st.number_input("masukkan nilai sisi 1",0)
        sisi2 = st.number_input("masukkan nilai sisi 2",0)
        sisi3 = st.number_input("masukkan nilai sisi 3",0)
        if st.button("hitung", type="primary"):
            luas = 0.5 * alas * tinggi
            keliling = sisi1 + sisi2 + sisi3
            st.success(f"luas segitiga adalah: {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            st.balloons()

    case "jajar genjang":
        st.title("jajar genjang")
        st.markdown("menghitung 'luas' dan 'keliling' jajar genjang")
        alas = st.number_input("masukkan nilai alas",0)
        tinggi = st.number_input("masukkan nilai tinggi",0)
        sisi1 = st.number_input("masukkan nilai sisi 1",0)
        sisi2 = st.number_input("masukkan nilai sisi 2",0)
        if st.button("hitung", type="primary"):
            luas = alas * tinggi
            keliling = 2 * (sisi1 + sisi2)
            st.success(f"luas jajar genjang adalah: {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            st.balloons()

    case _:
        st.error("pilihan tidak valid")


    