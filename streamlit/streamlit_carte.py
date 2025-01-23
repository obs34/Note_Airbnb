import pandas as pd
import geopandas as gpd

import folium
import streamlit as st
from streamlit_folium import st_folium

# donnees_iris = pd.read_csv(r"résultat\note\kmeans_données_cluster_nom.csv", encoding='utf-8', sep=';')
# carte_iris = gpd.read_file(r"données\couches\georef-herault-iris.geojson")
# data = pd.merge(donnees_iris, carte_iris[["code_officiel_iris", "geometry"]], left_on='INSEE', right_on='code_officiel_iris') # , how='right'
# opacity = 0.8
# # https://loading.io/color/feature/Set3-12/
# style = {
#     0 : {"fillColor": "#d9d9d9", "weight": 2, "color": "black", "fillOpacity": opacity},
#     1 : {"fillColor": "#8dd3c7", "weight": 2, "color": "black", "fillOpacity": opacity},
#     2 : {"fillColor": "#ffffb3", "weight": 2, "color": "black", "fillOpacity": opacity},
#     3 : {"fillColor": "#bebada", "weight": 2, "color": "black", "fillOpacity": opacity},
#     4 : {"fillColor": "#fb8072", "weight": 2, "color": "black", "fillOpacity": opacity},
#     5 : {"fillColor": "#80b1d3", "weight": 2, "color": "black", "fillOpacity": opacity},
#     6 : {"fillColor": "#fdb462", "weight": 2, "color": "black", "fillOpacity": opacity},
#     7 : {"fillColor": "#b3de69", "weight": 2, "color": "black", "fillOpacity": opacity},
#     8 : {"fillColor": "#fccde5", "weight": 2, "color": "black", "fillOpacity": opacity},
#     9 : {"fillColor": "#bc80bd", "weight": 2, "color": "black", "fillOpacity": opacity},
#     10 : {"fillColor": "#ccebc5", "weight": 2, "color": "black", "fillOpacity": opacity},
#     11 : {"fillColor": "#ffed6f", "weight": 2, "color": "black", "fillOpacity": opacity}
# }
# data["style"] = [style[c] for c in data["cluster"]]

# # Convertir en GeoDataFrame
# gdf = gpd.GeoDataFrame(data, geometry='geometry')


# m = folium.Map(location=[43.59370235053383, 3.681190006250655], zoom_start=9)  # Centre de l'Hérault

# tooltip = folium.GeoJsonTooltip(
#     fields=["nom", "INSEE", "cluster"],
#     aliases=["Nom:", "Code INSEE:", "N° catégorie:"],
#     localize=True,
#     sticky=False,
#     labels=True,
#     style="""
#         background-color: #F0EFEF;
#         border: 2px solid black;
#         border-radius: 3px;
#         box-shadow: 3px;
#     """,
#     max_width=800,
# )

# # Rajouter moyenne cluster + moyenne département
# popup = folium.GeoJsonPopup(
#     fields=['INSEE', 'nom', 
#             'croissance_relative_RP_log', 'deriv_plpr', 'point_vac', 'taux_d_implantation',
#             'taux_d_implantation_parc_tot', 'part_rs', 'tour_log',
#             'indicateur_marche_2023', 'evoli', 'rev_disp_med',
#             'cluster'],
#     aliases=['Code INSEE:', 'Nom:', 
#             'Croissance relative des RP par rapport aux logements:', 'Evolution du parc locatif privé:', 
#             'Evolution du parc de logement vacant:', 'Taux d\'implantation d\'Airbnb loués plus de 120 jours dans le parc habitable:',
#             'Taux d\'implantation d\'Airbnb dans le parc total:', 'Part des résidences secondaires:', 'Nombre d\'offre touristique par logement:',
#             'Indicateur marché immobilier 2023:', 'Evolution des prix immobilier:', 'Revenu disponible médian:',
#             'N° catégorie:'],
#     localize=True,
#     labels=True,
#     style="background-color: yellow;",
# )

# # folium.GeoJson(data).add_to(m)
# folium.GeoJson(
#     gdf,
#     # zoom_on_click=True, # Zoomer sur le polygone au clic
#     # style_function=lambda feature: style[feature["properties"]["cluster"]]
#     tooltip=tooltip,
#     popup=popup,
# ).add_to(m)

# # Fonction pour créer une légende en HTML
# def add_legend(map_obj, title, legend_dict):
#     legend_html = f"""
#     <div style="
#         position: fixed; 
#         top: 50px; right: 50px; 
#         width: 250px; height: auto; 
#         background-color: white; 
#         border:2px solid grey; z-index:9999; font-size:14px;
#         padding: 10px;">
#         <b>{title}</b><br>
#     """
#     for label, color in legend_dict.items():
#         legend_html += f"""
#         <i style="background: {color}; width: 15px; height: 15px; 
#         display: inline-block; margin-right: 5px;"></i> {label}<br>
#         """
#     legend_html += "</div>"

#     # Ajouter la légende à la carte
#     map_obj.get_root().html.add_child(folium.Element(legend_html))

# # Dictionnaire de légende (clusters et leurs couleurs)
# legend_dict = {
#     "Cluster 1": "#8dd3c7",
#     "Cluster 2": "#ffffb3",
#     "Cluster 3": "#bebada",
#     "Cluster 4": "#fb8072",
#     "Cluster 5": "#80b1d3",
#     "Cluster 6": "#fdb462",
#     "Cluster 7": "#b3de69",
#     "Cluster 8": "#fccde5",
#     "Cluster 9": "#bc80bd",
#     "Cluster 10": "#ccebc5",
#     "Cluster 11": "#ffed6f",
# }

# # Appelle la fonction pour ajouter la légende à la carte
# add_legend(m, "Légende des Clusters", legend_dict)

st.set_page_config(page_title="Votre Dashboard", layout="wide")

# Titre de l'application
st.title("Dashboard avec une Carte Folium")

# Section des paramètres
st.sidebar.header("Paramètres")
latitude = st.sidebar.slider("Latitude", -90.0, 90.0, 48.8566)  # Valeur par défaut : Paris
longitude = st.sidebar.slider("Longitude", -180.0, 180.0, 2.3522)  # Valeur par défaut : Paris
zoom = st.sidebar.slider("Zoom", 1, 18, 12)

# Création de la carte avec Folium
map_folium = folium.Map(location=[latitude, longitude], zoom_start=zoom)

# Ajouter un marqueur
folium.Marker(
    [latitude, longitude],
    popup="Vous êtes ici",
    tooltip="Cliquez pour plus d'informations",
).add_to(map_folium)

# Afficher la carte avec Streamlit
st.write("## Carte interactive")
st_folium(map_folium, width=700, height=500)

# Section de données additionnelles
st.write("## Informations complémentaires")
st.write(
    f"Coordonnées actuelles : ({latitude}, {longitude}) avec un zoom de {zoom}."
)
