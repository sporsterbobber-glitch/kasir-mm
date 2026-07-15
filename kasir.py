import streamlit as st

st.set_page_config(page_title="Kasir Minimarket", page_icon="🛒", layout="centered")

st.title("🛒 Aplikasi Kasir Minimarket")
st.caption("Hitung transaksi + diskon otomatis")

# === INPUT ===
with st.form("form_kasir"):
    st.subheader("Input Transaksi")
    
    nama_pembeli = st.text_input("Nama Pembeli *")
    nama_barang = st.text_input("Nama Barang *")
    
    col1, col2 = st.columns(2)
    with col1:
        harga_barang = st.number_input("Harga Barang", min_value=0, step=1000)
    with col2:
        jumlah_barang = st.number_input("Jumlah Barang", min_value=0, step=1)

    hitung = st.form_submit_button("Hitung Total Bayar")

# === PROSES ===
def hitung_diskon(total):
    # Ketentuan Diskon:
    # Total >= 500.000 -> Diskon 10%
    # Total >= 250.000 -> Diskon 5% 
    # Selain itu -> Tidak ada diskon
    if total >= 500000:
        return total * 0.10, "10%"
    elif total >= 250000:
        return total * 0.05, "5%"
    else:
        return 0, "0%"

# === OUTPUT ===
if hitung:
    if nama_pembeli.strip() == "" or nama_barang.strip() == "":
        st.error("Nama Pembeli dan Nama Barang wajib diisi!")
    else:
        # Hitung
        subtotal = harga_barang * jumlah_barang
        nilai_diskon, persen_diskon = hitung_diskon(subtotal)
        total_bayar = subtotal - nilai_diskon

        st.divider()
        st.subheader("🧾 Struk Belanja")

        st.write(f"*Nama Pembeli:* {nama_pembeli}")
        st.write(f"*Barang:* {nama_barang}")
        st.write(f"*Harga x Jumlah:* Rp{harga_barang:,} x {jumlah_barang}")

        st.divider()
        col1, col2, col3 = st.columns(3)
        col1.metric("Subtotal", f"Rp{subtotal:,}")
        col2.metric("Diskon", f"Rp{int(nilai_diskon):,}", f"-{persen_diskon}")
        col3.metric("Total Bayar", f"Rp{int(total_bayar):,}")

        # Keterangan diskon
        if persen_diskon == "10%":
            st.success("Selamat! Kamu dapat diskon 10% karena belanja >= Rp500.000")
        elif persen_diskon == "5%":
            st.info("Kamu dapat diskon 5% karena belanja >= Rp250.000")
        else:
            st.write("Belanja < Rp250.000, belum dapat diskon")