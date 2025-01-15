import matplotlib.pyplot as plt
import numpy as np
import matplotlib.tri as tri
import matplotlib.dates as mdates
import json
import pandas as pd
import plotly.express as px
import js
import pyodide
from pyodide.http import pyfetch

from data_handler import data_handler
from pyscript import document
from pyscript import display
from http_handler import http_handler

#IMPORTANT - All classes and packages used in the pythin files must be included in the pyscript.json file
#see file and packages in pyscript.json






# Iris-Daten aus Plotly Express laden
umfrage_handler = data_handler("umfragewerte")
df = umfrage_handler.extract_mean_of_survey(umfrage_handler)
print(df.index)
print(df)

# Erstellen eines interaktiven Scatterplots
fig = px.scatter(df, x= df.index, y= df.columns , title="Aktuelle Umfragewerte")


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