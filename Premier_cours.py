# Importation des libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
# Affichage de texte
st.title("Bienvenue sur Streamlit !")
st.header("Un framework pour créer des applications web avec Python")
st.write("Ceci est un texte affiché avec la fonction `write` de Streamlit.")

# Afficher un tableau

df = pd.DataFrame({
    "Nom": ["Alice", "Bob", "Charlie"],
    "Âge": [25, 30, 35],
    "Score": [88, 92, 79]
})
 
st.dataframe(df)  # Affiche un tableau interactif
st.table(df)  # Affiche un tableau statique

if st.button("Clique-moi"):
    st.write("Bouton cliqué !")

if st.checkbox("Afficher un message"):
    st.write("Vous avez coché la case !")

option = st.selectbox("Choisissez une option", ["Option 1", "Option 2", "Option 3"])
st.write("Vous avez sélectionné :", option)

valeur = st.slider("Choisissez une valeur", 0, 100, 50)
st.write("Valeur sélectionnée :", valeur)


# Data entry
age = st.number_input("Entrez votre âge", min_value=1, max_value=100, value=25)
 
st.write("Votre âge est :", age)
nom = st.text_input("Entrez votre nom")
st.write("Bonjour", nom)
poids= st.number_input("Entrez votre poids")
 
l=[]
l.extend([nom, age, poids])
 
df2= pd.DataFrame(l)
 
st.dataframe(df2)

# Graphiques
df3 = pd.DataFrame({     "x": np.linspace(0, 10, 100),     "y": np.sin(np.linspace(0, 10, 100)) }) # Créer un graphique interactif avec Plotly
fig = px.line(df3, x="x", y="y", title="Graphique en ligne avec Plotly") # Afficher le graphique dans Streamlit 
st.plotly_chart(fig)
 
 # Charger un dataset intégré de Plotly
df = px.data.iris()
 
# Créer un scatter plot
fig = px.scatter(df, x="sepal_width", y="sepal_length",
                 color="species", title="Scatter Plot des fleurs d'Iris")
 
# Afficher dans Streamlit
st.plotly_chart(fig)

# Charger un dataset intégré
df = px.data.gapminder()
 
# Sélecteur interactif pour choisir un pays
pays = st.selectbox("Sélectionnez un pays", df["country"].unique())
variable= st.selectbox("Sélectionnez une variable", df.columns[3:6])
 
# Filtrer les données du pays sélectionné
df_pays = df[df["country"] == pays]
 
# Créer un graphique en barres de l'espérance de vie
fig = px.bar(df_pays, x="year", y=variable, title=f"Évolution de l'espérance de vie en {pays}")
 
# Afficher dans Streamlit
st.plotly_chart(fig)
 
st.dataframe(df)

# Charger un dataset avec des données géographiques

df = px.data.gapminder()
 
# Filtrer l'année 2007

df_2007 = df[df["year"] == 2007]
 
# Créer une carte avec les données

fig = px.choropleth(df_2007, locations="iso_alpha", color="lifeExp",

                     hover_name="country", color_continuous_scale=px.colors.sequential.Plasma,

                     title="Espérance de vie par pays (2007)")
 
# Afficher la carte dans Streamlit

st.plotly_chart(fig)

# Sidebar
st.sidebar.title("Options")
choix = st.sidebar.selectbox("Choisis", ["Option 1", "Option 2"])
st.write(f"Choix depuis la sidebar : {choix}")

# Import data
df=pd.read_excel(r"C:\Users\MIVS\Documents\Vs code\BD finale.xlsx") # Changer le chemin de la base de données
st.dataframe(df)