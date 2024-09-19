import streamlit as st
import speedtest

st.title("İnternet Hız Testi")

st_test = speedtest.Speedtest()

if st.button("Hız Testini Başlat"):
    st.write("Test yapılıyor, lütfen bekleyin...")
    
    # Sunucu listesi ve en iyi sunucuyu seçme
    st_test.get_servers()
    en_iyi_server = st_test.get_best_server()
    st.write(f"Seçilen sunucu: {en_iyi_server['host']} ({en_iyi_server['country']})")

    # Download hızı
    download_hizi = st_test.download() / 1000000  # Mbps'e çevir
    st.write(f"İndirme Hızı: {download_hizi:.2f} Mbps")

    # Upload hızı
    upload_hizi = st_test.upload() / 1000000  # Mbps'e çevir
    st.write(f"Yükleme Hızı: {upload_hizi:.2f} Mbps")

    # Ping süresi
    ping = st_test.results.ping
    st.write(f"Ping: {ping:.2f} ms")
