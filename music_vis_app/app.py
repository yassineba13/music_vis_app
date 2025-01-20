import streamlit as st

# Première commande Streamlit : set_page_config()
st.set_page_config(page_title="Music Insights", page_icon="🎵")

from music_vis_app.home import show_home
from music_vis_app.dashboard import show_dashboard  # Assurez-vous que vous avez une fonction show_dashboard dans dashboard.py



# Changer le fond de la page en blanc
st.markdown(
    """
    <style>
        body {
            background-color: white;
        }
        .stButton > button {
            background-color: #4CAF50; 
            color: white;
            padding: 10px 30px;
            font-size: 16px;
            border-radius: 5px;
            border: none;
            width: 200px;
            margin: auto;
            display: block;
        }
        .stButton > button:hover {
            background-color: #45a049;
        }
        h1, h2 {
            text-align: center;
        }
        p {
            text-align: center;
            font-size: 18px;
            color: #555;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Titre de l'application
st.markdown(
    """
    <h1>Music Insights 🎶</h1>
    <h2>Découvrez quel genre musical maximise les ventes</h2>
    """,
    unsafe_allow_html=True,
)

# Brève description avec un texte engageant
st.markdown(
    """
    <p>Bienvenue sur Music Insights ! Cette application vous aide à analyser les styles musicaux et leurs caractéristiques.
        Explorez quel genre peut maximiser les ventes dans l'industrie musicale.</p>
    """,
    unsafe_allow_html=True,
)

# Espacement entre l'image et le bouton
st.markdown("<br><br>", unsafe_allow_html=True)

# Bouton centré pour accéder au Dashboard
if st.button("Accéder au Dashboard", key="dashboard_button", help="Cliquez ici pour commencer l'analyse !"):
    st.session_state.page = "dashboard"  # Met à jour la page à afficher
    st.rerun()  # Recharger la page pour afficher le dashboard

# Page d'affichage conditionnelle
if "page" not in st.session_state:
    st.session_state.page = "home"  # Page d'accueil par défaut

# Afficher le contenu de la page en fonction de l'état de la session
if st.session_state.page == "home":
    # Afficher la page d'accueil
    show_home()
elif st.session_state.page == "dashboard":
    # Afficher le dashboard avec les visualisations
    show_dashboard()  # Fonction dans le fichier dashboard.py pour afficher les visualisations
