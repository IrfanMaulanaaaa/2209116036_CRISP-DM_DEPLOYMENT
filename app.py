import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import *
from function import *
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split


df = pd.read_csv('Data_for_deploy (1).csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/IrfanMaulanaaaa/Data-Mining-2024/main/Data_Cleaned%20(3).csv')
with st.sidebar :
    selected = option_menu('Housing',['Introducing','Data Distribution','Proportion','Comparison','Predict'],default_index=0)

if (selected == 'Introducing'):
    
    st.title("Analisis dan Prediksi Harga Perumahan")
    st.header("Dataset")
    url = "Data_for_deploy (1).csv"
    df = pd.read_csv(url)
    st.write(df)
    st.write("Cleaned housing dataset")
    desc_stats = df.describe()

    st.subheader("Descriptive Statistic Information")
    # Display descriptive statistics in Streamlit
    st.write("Descriptive Statistics:")
    st.dataframe(desc_stats)
    st.write("#### Rata-rata (Mean):")
    st.write("Harga rata-rata properti adalah sekitar $4,224,738, dengan luas area rata-rata sekitar 4,630 sqft (429.56 meter persegi). Ini memberikan gambaran tentang harga properti dan ukurannya secara umum.")

    st.write("#### Standar Deviasi (Std):")
    st.write("Standar deviasi harga properti ($1,274,420) menunjukkan seberapa jauh data tersebar dari rata-rata. Semakin tinggi nilai standar deviasi, semakin besar variasi harga properti di dataset.")

    st.write("#### Nilai Minimum dan Maksimum (Min dan Max):")
    st.write("Harga properti bervariasi antara $1,750,000 dan $8,043,000, sedangkan luas area berkisar antara 1,650 sqft (153.29 meter persegi) dan 9,800 sqft (910.23 meter persegi). Ini menunjukkan variasi ekstrem dalam harga dan ukuran properti di dataset.")

    st.write("#### Kuartil (25%, 50%, 75%):")
    st.write("Kuartil bawah (25%) harga properti adalah sekitar $3,290,000, sementara kuartil atas (75%) adalah sekitar $5,026,000. Ini memberikan gambaran tentang distribusi harga properti di dataset, serta kisaran harga yang mungkin diharapkan untuk properti dengan kualitas berbeda.")


if (selected == 'Data Distribution'):
    st.header("Data Distribution")
    scatter_plot(df)
    
if (selected == 'Proportion'):
    st.title('Proportion')
    proportion(df)

if (selected == 'Comparison'):
    st.title('Comparison')
    Comparison(df)

if (selected == 'Predict'):
    data2 = "https://raw.githubusercontent.com/IrfanMaulanaaaa/Data-Mining-2024/main/Data_Cleaned%20(3).csv"
    df2 = pd.read_csv(data2)
    st.write("Cleaned housing dataset")
    x = df2.drop('price', axis=1)
    y = df2['price']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    scaler = MinMaxScaler()

    x_train_norm = scaler.fit_transform(x_train)

    x_test_norm = scaler.transform(x_test)
    # # Memisahkan fitur dan target
    dtc = DecisionTreeClassifier()
    dtc.fit(x_train_norm, y_train)
    # Mengambil input dari pengguna dan menyimpannya dalam variabel new_data
    new_data = {
        'area': [st.number_input('Luas Area', min_value=0, step=100)],  
        'bedrooms': [st.number_input('Jumlah Kamar Tidur', min_value=1, step=1)],  
        'bathrooms': [st.number_input('Jumlah Kamar Mandi', min_value=1, step=1)],  
        'stories': [st.number_input('Jumlah Lantai', min_value=1, step=1)],  
        'total_building_area': [st.number_input('Total Luas Bangunan', min_value=0, step=100)],  
        'mainroad_no': [st.number_input('Rumah Berada di Jalan Utama (0: Tidak, 1: Ya)', min_value=0, max_value=1, step=1)],  
        'mainroad_yes': [1],  
        'guestroom_no': [st.number_input('Rumah Memiliki Kamar Tamu (0: Tidak, 1: Ya)', min_value=0, max_value=1, step=1)],  
        'guestroom_yes': [1],
        'basement_no': [st.number_input('Rumah Tidak Memiliki Ruang Bawah Tanah (0: Tidak, 1: Ya)', min_value=0, max_value=1, step=1)],  
        'basement_yes': [1],
        'hotwaterheating_no': [st.number_input('Rumah Memiliki Pemanas Air (0: Tidak, 1: Ya)', min_value=0, max_value=1, step=1)],  
        'hotwaterheating_yes': [1],
        'airconditioning_no': [st.number_input('Rumah Memiliki AC (0: Tidak, 1: Ya)', min_value=0, max_value=1, step=1)],  
        'airconditioning_yes': [1],
        'prefarea_no': [st.number_input('Rumah Tidak Berada di Area Preferensi (0: Tidak, 1: Ya)', min_value=0, max_value=1, step=1)],  
        'prefarea_yes': [1],
        'furnishingstatus_furnished': [st.number_input('Rumah Berperabot Lengkap (1: Ya, 0: Tidak)', min_value=0, max_value=1, step=1)],  
        'furnishingstatus_semi-furnished': [0],  
        'furnishingstatus_unfurnished': [0], 
    }


    # Convert new_data to a DataFrame
    new_df = pd.DataFrame.from_dict(new_data)


    # with open('dtc (1).pkl', 'rb') as file:
    #     loaded = pickle.load(file)


    # predicted_price = loaded.predict(new_df)

    predicted_price = dtc.predict(new_df)

    # Perform house price prediction with the trained Decision Tree Classifier model
    # predicted_price = dtc.predict(new_df)

    # Display the prediction result
    st.write("Prediksi Harga Rumah:", predicted_price)

# if (selected == 'Clustering'):
#     st.title('Clustering!')
#     clustering(df)