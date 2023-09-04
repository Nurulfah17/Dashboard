import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

data = pd.read_csv("day.csv", delimiter=",")


def ubah_isi(data):
    data['season'] = data['season'].astype('category')
    data['season'] = data['season'].cat.rename_categories(['Musim Dingin', 'Musim Semi', 'Musim Panas', "Musim Gugur"])
    data['mnth'] = data['mnth'].astype('category')
    data['mnth'] = data['mnth'].cat.rename_categories(
        ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'])
    data['yr'] = data['yr'].astype('category')
    data['yr'] = data['yr'].cat.rename_categories(['2011', '2012'])
    return data


def create_bar_plot(data, x, y, title, x_label, y_label, figsize=(10, 5)):
    plt.figure(figsize=figsize)
    sns.barplot(y=y, x=x, data=data.sort_values(by=y, ascending=False), palette="Blues")
    plt.title(title, loc="center", fontsize=15)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.tick_params(axis='x', labelsize=12)

    return plt


# Streamlit app
st.header('Dashboard Penyewa Sepeda :sparkles:')
st.subheader("Jumlah Penyewa Sepeda")

with st.sidebar:
    tahun_terpilih = st.selectbox('Pilih Tahun:', data['yr'].unique())

# Check if the selected year exists in the dataset
# Streamlit app
st.header('Bike Sharing Dashboard :sparkles:')
st.subheader("Jumlah Penyewa Sepeda")

with st.sidebar:
    tahun_terpilih = st.selectbox('Pilih Tahun:', data['yr'].unique())

# Check if the selected year exists in the dataset
if str(tahun_terpilih) in data['yr'].astype(str).values:
    main_data = data[data['yr'] == str(tahun_terpilih)]

    # Check if there's data to display in the bar plots
    if not main_data.empty:
        # Create bar plot for bike rentals by season
        st.subheader("Jumlah Penyewa Sepeda Berdasarkan Musim")
        season_plot = create_bar_plot(main_data, x="season", y="cnt", title="Jumlah Penyewa Sepeda Berdasarkan Musim",
                                      x_label="Musim", y_label="Jumlah")

        # Display the season plot using Streamlit
        st.pyplot(season_plot)

        # Create bar plot for bike rentals by month
        st.subheader("Jumlah Penyewa Sepeda Berdasarkan Bulan")
        month_plot = create_bar_plot(main_data, x="mnth", y="cnt", title="Jumlah Penyewa Sepeda Berdasarkan Bulan",
                                     x_label="Bulan", y_label="Jumlah")

        # Display the month plot using Streamlit
        st.pyplot(month_plot)
    else:
        st.warning("Tidak ada data yang tersedia untuk tahun yang dipilih.")
else:
    st.error("Tahun yang dipilih tidak ada dalam dataset. Silakan pilih tahun lain.")

