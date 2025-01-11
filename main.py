import matplotlib.pyplot as plt
import numpy as np
import matplotlib.tri as tri
import matplotlib.dates as mdates
import json
import pandas as pd
import plotly.express as px
import js

#from pyodide.ffi import to_js as _to_js
#from pyweb import pydom
from pyscript import document
from pyscript import display



# Iris-Daten aus Plotly Express laden
df = px.data.iris()

# Erstellen eines interaktiven Scatterplots
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species', title="Interaktiver Scatterplot")

# Diagramm anzeigen (interaktiv)
display(fig, target="umfrage_graph")

"""
def to_js(data):
    if data is None:
        return None
    return _to_js(data, dict_converter=js.Object.fromEntries)

def fig_to_js(fig, config=None):
    data_json = fig.to_json(validate=False)
    if not config:
        return js.JSON.parse(data_json)
    if not isinstance(config,dict):
        raise TypeError(f'config must be a dict or None')

    data = json.loads(data_json)
    data['config'] = config
    return to_js(data)

def plot(fig, target="umfrage_graph", config=None):
    js.window.Plotly.newPlot(target, fig_to_js(fig, config=config))

df = px.data.stocks()
fig = px.line(df,x ='date', y=df.columns, hover_data={'date':'%B %d, %Y'}, title='stocks', template='plotly_dark',)
fig.update_xaxes(dTick='M1',tickformat='%b\n%Y',ticklabelmode='period')

#remove the "loading..." message
pydom['#placeholder'][0].add_class('d-none')

#display the responsive plot. and hide the plotly logo from the modebar
try:
    plot(fig, config={'displaylogo': False, 'responsive': True, 'scrollZoom': True})
except Exception as e:
    import traceback
    tb = ''.join(traceback.TracebackException.from_exception(e).format())
    js.document.body.innerHTML = f'<pre>{tb}</pre>'"""


#test of pandas with plotly

#header = "Umfragewerte der größeren Parteien zur Bundestagsewahl"
#subheader = "neueste Umfragewerte Quelle (dawum.de)"
#description = "Die Grafik zweigt die neuesten Werte aus verschiedenen Umfrageinstituten in Prozent"

#display(header, target="header")
#display(subheader, target="subheader")
#display(description, target="description")

#umfrage_dataf = 1

#umfrage_graph = px.line(umfrage_dataf,x = "Datum der Umfrage", y = "Prozent", width=800, height=400, template = "plotly_white")

#display(umfrage_graph, target="umfrage_graph")

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