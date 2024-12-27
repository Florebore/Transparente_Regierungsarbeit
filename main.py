import matplotlib.pyplot as plt
import numpy as np
import matplotlib.tri as tri
import matplotlib.dates as mdates
from pyscript import document
from pyscript import display
import json
import urllib.request


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

def convert_json(String json):




def get_request(String http):

    contents = urllib.request.urlopen("http://example.com/foo/bar").read()
