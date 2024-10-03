import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

day_df = pd.read_csv('day_df.csv')
hour_df = pd.read_csv('hour_df.csv')

st.title("Bike Sharing Data Analysis Dashboard")

st.sidebar.title("Memilih Visualisasi")
option = st.sidebar.selectbox(
    'Pilih visualisasi',
    ['Cuaca vs Jumlah Penyewaan', 'Hari Kerja vs Hari Libur', 'Tren Penyewaan Bulanan'])

if option == 'Cuaca vs Jumlah Penyewaan':
    st.header("Pengaruh Cuaca terhadap Jumlah Penyewaan Sepeda")
    
    fig, ax = plt.subplots()
    sns.barplot(x='weathersit', y='cnt', data=day_df, palette='Set2', ax=ax)
    ax.set_title('Cuaca vs Jumlah Penyewaan Sepeda')
    ax.set_xlabel('Kondisi Cuaca')
    ax.set_ylabel('Jumlah Penyewaan')
    st.pyplot(fig)

elif option == 'Hari Kerja vs Hari Libur':
    st.header("Perbandingan Penyewaan Sepeda: Hari Kerja vs Hari Libur")
    
    fig, ax = plt.subplots()
    sns.barplot(x='workingday', y='cnt', data=day_df, palette='Set1', ax=ax)
    ax.set_title('Hari Kerja vs Hari Libur - Jumlah Penyewaan Sepeda')
    ax.set_xlabel('Hari Kerja vs Hari Libur')
    ax.set_ylabel('Jumlah Penyewaan')
    st.pyplot(fig)

elif option == 'Tren Penyewaan Bulanan':
    st.header("Tren Penyewaan Sepeda Bulanan dalam Dua Tahun")

    monthly_counts = day_df.groupby(by=["mnth", "yr"]).agg({"cnt": "sum"}).reset_index()

    fig, ax = plt.subplots()
    sns.lineplot(
        data=monthly_counts,
        x="mnth",
        y="cnt",
        hue="yr",
        palette="Set2",
        marker="o",
        ax=ax)
    ax.set_title("Trend Sewa Sepeda Bulanan")
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penyewaan')
    ax.legend(title="Tahun", loc="upper right")
    plt.tight_layout()
    st.pyplot(fig)