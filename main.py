import matplotlib.pyplot as plt
import numpy as np
import matplotlib.tri as tri
import matplotlib.dates as mdates
import json
import pandas as pd
import plotly.express as px
import js
from data_handler import data_handler
from pyscript import document
from pyscript import display
from http_handler import http_handler

#IMPORTANT - All classes and packages used in the python files must be included in the pyscript.json file
#see file and packages in pyscript.json


# Umfragedaten aus Plotly Express laden
umfrage_handler = data_handler("umfragewerte")
df = umfrage_handler.extract_mean_of_survey(umfrage_handler)

# Erstellen eines interaktiven Scatterplots1
#fig = px.scatter(df, x= df.index, y= df.columns , title="Aktuelle Umfragen zur Bundestagswahl")
#Hier muss Grafik geupdated werden
#fig.update_layout(
#    xaxis_title="Befragungen",
#    yaxis_title="Prozent",
#    legend_title="Parteien",
#    font=dict(
#        family="Roboto, monospace",
#        size=16
#    )
#)

# Diagramm anzeigen (interaktiv)
#display(fig, target="umfrage_graph")

# Erstellen eines interaktiven Scatterplots
fig = px.line(df, markers= True, color_discrete_map ={  # replaces default color mapping by value
                 "Christlich Demokratische Union / Christlich-Soziale Union": "#222A2A",
                "Alternative für Deutschland": "blue", "Sozialdemokratische Partei Deutschlands": "red",
                  "Bündnis 90/Die Grünen": "green", "sonstige Parteien": "grey", "Bündnis Sahra Wagenknecht": "purple",
                 "Freie Demokratische Partei": "yellow", "Die Linke": "magenta",
                  "Freie Wähler": "#3366CC"}
              )

#Hier muss Grafik geupdated werden, um das Design zu ändern
fig.update_layout(
font={"family": "Roboto, sans-serif", "size": 14},  # Font settings
    colorway=["#6200EA", "#03DAC5", "#018786", "#B00020"],  # Material Design colors
    paper_bgcolor="#F5F5F5",  # Background for the entire figure
    plot_bgcolor="#FFFFFF",  # Background for the chart area
    xaxis={
        "gridcolor": "#E0E0E0",  # Light gray gridlines
        "zerolinecolor": "#E0E0E0",  # Zero line color
        "title_font": {"size": 16},  # Font size for x-axis title
    },
    yaxis={
        "gridcolor": "#E0E0E0",  # Light gray gridlines
        "zerolinecolor": "#E0E0E0",  # Zero line color
        "title_font": {"size": 16},  # Font size for y-axis title
    },
    legend={
        "bgcolor": "rgba(255,255,255,0.8)",  # Semi-transparent legend background
        "bordercolor": "#E0E0E0",  # Light gray border for the legend
    },
    hovermode="x unified",  # Single hover label for x-axis
    hoverlabel={"font_size": 12, "font_family": "Roboto"},  # Hover font styling
    margin=dict(l=20, r=20, t=40, b=20),  # Adjust margins for clean spacing
    width=1500,
    height=500,
    xaxis_title="Befragungen",
    yaxis_title="Prozent",
    legend_title="Parteien"

)


# Example annotation for key insights
#fig.add_annotation(
#    x="2024-12-20",  # Replace with your data value
#    y=30,  # Replace with your data value
#    text="Beginn des Trends",
#    showarrow=True,
#    arrowhead=2,
#    arrowsize=1,
#    arrowcolor="#6200EA",
#    font={"color": "#222A2A", "size": 14}
#)

# Diagramm anzeigen (interaktiv)
display(fig, target="umfrage_graph")


#Button Change test an test of Matpolotlib in combination with button click
def se(self):
    print("Ja")
    button_c = document.getElementById("plot-button")
    button_c.innerText = "Jetzt"
    # First create the x and y coordinates of the points.
    fig_party_survey = plt.figure()
    fig_party_survey, ax = plt.subplots()
    ax.plot([10,20,30,40,50,60,70,80,90,100])
    ax.set_title("Umfragewerte der Parteien")
    ax.set_xlabel("Zeitverlauf")
    ax.set_ylabel("Prozent")
    ax.legend()
    display(fig_party_survey, target="party_survey_mpl")