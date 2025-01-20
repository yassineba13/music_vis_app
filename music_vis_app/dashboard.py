import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données
@st.cache
def load_data():
    # Assurez-vous de bien mettre le chemin du fichier csv relatif à votre projet
    data = pd.read_csv(r"C:\Users\HP\music_vis_app\src\music_vis_app\Data\spotify_tracks.csv")
    return data

def show_dashboard():
    # Charger les données
    df = load_data()



    # Calcul de la durée moyenne par genre (conversion de ms en minutes)
    df['duration_min'] = df['duration_ms'] / 60000
    avg_duration_per_genre = df.groupby('track_genre')['duration_min'].mean().sort_values()

    plt.figure(figsize=(12, 6))
    sns.barplot(x=avg_duration_per_genre.index, y=avg_duration_per_genre.values, palette="coolwarm")
    plt.xticks(rotation=90)
    plt.title("Durée moyenne des tracks par genre musical")
    plt.xlabel("Genre musical")
    plt.ylabel("Durée moyenne (minutes)")
    st.pyplot(plt)

    plt.figure(figsize=(8, 6))
    sns.boxplot(x=df['explicit'], y=df['popularity'], palette="Set2")
    plt.title("Distribution de la popularité selon le caractère explicite des tracks")
    plt.xlabel("Explicit (0 = Non, 1 = Oui)")
    plt.ylabel("Popularité")
    st.pyplot(plt)

    avg_popularity_time_signature = df.groupby('time_signature')['popularity'].mean().sort_index()

    plt.figure(figsize=(8, 5))
    sns.barplot(x=avg_popularity_time_signature.index, y=avg_popularity_time_signature.values, palette="muted")
    plt.title("Popularité moyenne en fonction du time signature")
    plt.xlabel("Time Signature")
    plt.ylabel("Popularité moyenne")
    st.pyplot(plt)


    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=df['tempo'], y=df['popularity'], alpha=0.5, color='dodgerblue')
    sns.regplot(x=df['tempo'], y=df['popularity'], scatter=False, color='red')  # Ligne de tendance
    plt.title("Relation entre le tempo et la popularité des tracks")
    plt.xlabel("Tempo (BPM)")
    plt.ylabel("Popularité")
    st.pyplot(plt)

