import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO




def scatter_plot(df):
    area_range = st.sidebar.slider('Rentang Luas Area (sqft)', min_value=0, max_value=10000, value=(0, 10000))

# Menyaring data berdasarkan rentang luas area yang dipilih
    filtered_data = df[(df['area'] >= area_range[0]) & (df['area'] <= area_range[1])]

# Histogram frekuensi persebaran data perumahan berdasarkan luas area yang dipilih
    st.subheader('Histogram Luas Area Properti')
    plt.figure(figsize=(10, 6))
    sns.histplot(filtered_data['area'], bins=30, kde=True, color='skyblue')
    plt.xlabel('Luas Area (sqft)')
    plt.ylabel('Frekuensi')
    hist_plot = plt.gcf()  # Simpan plot dalam variabel
    st.pyplot(hist_plot)
    st.write("Rentang luas area 302.32 m² hingga 371.61 m² adalah area yang paling umum untuk properti di dataset ini. Hal ini menunjukkan bahwa properti dengan ukuran ini memiliki frekuensi tertinggi dalam data yang diamati.")
    st.write("Pemilik properti atau agen real estat dapat menggunakan informasi ini untuk menyesuaikan strategi pemasaran atau harga properti mereka. ")
    # Scatter plot harga perumahan terhadap luas area yang dipilih
    st.subheader('Scatter Plot Harga Perumahan vs. Luas Area')
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='area', y='price', data=filtered_data)
    plt.xlabel('Luas Area (sqft)')
    plt.ylabel('Harga Perumahan')
    scatter_plot = plt.gcf()  # Simpan plot dalam variabel
    st.pyplot(scatter_plot)
    area_counts = df['area'].value_counts().reset_index()
    area_counts.columns = ['Luas Area', 'Frekuensi']

    # Tampilkan tabel hasil insight di Streamlit
    st.write("## Insight: Frekuensi Persebaran Data Rumah Berdasarkan Luas Area")
    st.write(area_counts)
    st.write("menunjukkan bahwa luas area 3000 adalah yang paling umum di antara data rumah yang diamati. Ini bisa diartikan bahwa luas area 3000 memiliki popularitas yang tinggi di pasar perumahan yang dianalisis.")
    st.write("Mengetahui bahwa luas area 3000 adalah yang paling umum, perusahaan real estat atau agen pemasaran dapat membagi pasar mereka berdasarkan luas area, dengan menargetkan lebih banyak upaya pemasaran pada properti dengan luas area sekitar 3000.")
def proportion(df):
    prefarea_counts = df['prefarea'].value_counts()

# Buat pie chart untuk preferensi area
    fig_prefarea, ax_prefarea = plt.subplots()
    ax_prefarea.pie(prefarea_counts, labels=prefarea_counts.index, autopct='%1.1f%%', startangle=140)
    ax_prefarea.set_title('Proporsi Preferensi Area')
    ax_prefarea.axis('equal')  # Memastikan pie chart berbentuk lingkaran

    # Tampilkan pie chart di Streamlit
    st.write("## Pie Chart: Proporsi Preferensi Area")
    st.pyplot(fig_prefarea)
    st.write("proporsi rumah yang diluar area preferensi lebih banyak daripada didalam area preferensi sebanyak 78,5%")
    st.write("Dengan mengetahui bahwa proporsi rumah di luar area preferensi lebih banyak daripada yang berada di dalam area preferensi, kita dapat menyimpulkan bahwa ada potensi untuk meningkatkan strategi pemasaran di luar area preferensi. Mungkin ada kesempatan untuk menargetkan calon pembeli yang mencari rumah di lokasi tertentu yang tidak termasuk dalam area preferensi saat ini. ")
    # Hitung jumlah data di setiap kategori untuk kondisi furnishing
    furnishing_counts = df['furnishingstatus'].value_counts()

    # Buat pie chart untuk kondisi furnishing
    fig_furnishing, ax_furnishing = plt.subplots()
    ax_furnishing.pie(furnishing_counts, labels=furnishing_counts.index, autopct='%1.1f%%', startangle=140)
    ax_furnishing.set_title('Proporsi Kondisi Furnishing')
    ax_furnishing.axis('equal')  # Memastikan pie chart berbentuk lingkaran

    # Tampilkan pie chart di Streamlit
    st.write("## Pie Chart: Proporsi Kondisi Furnishing")
    st.pyplot(fig_furnishing)
    st.write("Kondisi perumahan semi-furnished memiliki proporsi yang paling banyak yaitu 42,5%")
    st.write("Hal ini bisa menjadi insight berharga bagi agen real estat atau pengembang properti untuk fokus pada penawaran rumah semi-furnished atau mempertimbangkan untuk menyediakan paket furnishing yang dapat menarik minat calon pembeli. ")
def Comparison (df):
# Hitung rata-rata fitur untuk setiap kelas
    st.write("## Bar Plot: Harga Rumah vs Preferensi Area")
    def plt_to_streamlit(plt):
        # Save plot to BytesIO object
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        # Return BytesIO object for Streamlit
        return buf
    plt.figure(figsize=(10, 6))
    sns.barplot(x='prefarea', y='price', data=df, palette='viridis')
    plt.title('Harga Rumah vs Preferensi Area')
    plt.xlabel('Preferensi Area')
    plt.ylabel('Harga Rumah')
    plt.grid(True)
    plt.tight_layout()

    # Convert plot to image
    image_streamlit = plt_to_streamlit(plt)

    # Display the image in Streamlit
    st.image(image_streamlit, use_column_width=True)

    # Hitung rata-rata harga rumah untuk setiap preferensi area
    avg_price_prefarea = df.groupby('prefarea')['price'].mean().reset_index()
    avg_price_prefarea.columns = ['Preferensi Area', 'Rata-rata Harga']
    avg_price_prefarea = df.groupby('prefarea')['price'].mean().reset_index()
    avg_price_prefarea.columns = ['Preferensi Area', 'Rata-rata Harga']

    # Tampilkan nilai angka
    st.write(avg_price_prefarea)
    st.write("Prefarea 'Yes' memiliki harga rumah yang lebih tinggi dibandingkan dengan prefarea 'No'. Ini menunjukkan bahwa lokasi preferensi (prefarea) memiliki pengaruh signifikan terhadap harga rumah. Kemungkinan besar, prefarea 'Yes' mungkin berada di lokasi yang lebih diinginkan atau memiliki fasilitas dan aksesibilitas yang lebih baik dibandingkan dengan prefarea 'No'.")
    st.write("Agen real estat dapat menyoroti keunggulan lokasi perumahan yang termasuk dalam area yang diinginkan dalam materi pemasaran mereka untuk menarik minat pembeli.")
    
    avg_price_furnishing = df.groupby('furnishingstatus')['price'].mean().reset_index()

    # Plotting dengan menggunakan barplot
    st.write("## Average House Price based on Furnishing Status")
    avg_price_furnishing = df.groupby('furnishingstatus')['price'].mean().reset_index()

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='furnishingstatus', y='price', data=avg_price_furnishing, palette='viridis', ax=ax)
    plt.xlabel('Furnishing Status')
    plt.ylabel('Average Price')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    st.write("Furnishing Status | Average Price")
    st.write(avg_price_furnishing)
    # Informasi interpretasi dari visualisasi boxplot
    st.write("- Rumah yang berperabot lengkap (fully furnished) dan semi-berperabot (semi-furnished) memiliki harga yang cenderung lebih tinggi, dengan perbedaan yang tidak signifikan antara keduanya. Hal ini terlihat dari tinggi kotak (jangkauan interkuartil) dan posisi median yang relatif serupa di antara keduanya.")
    st.write("- Sementara itu, rumah yang tidak berperabot lengkap (unfurnished) menunjukkan harga yang jauh lebih rendah dibandingkan dengan kedua kategori sebelumnya, dengan tinggi kotak yang lebih rendah dan posisi median yang lebih rendah pula.")
    st.write("Penjual atau agen real estat dapat menggunakan informasi ini untuk memahami bahwa pembeli mungkin memiliki preferensi yang mirip antara rumah yang berperabot lengkap dan semi-berperabot. Ini dapat menjadi dasar untuk segmentasi pasar dan strategi pemasaran yang lebih tepat.")


# 