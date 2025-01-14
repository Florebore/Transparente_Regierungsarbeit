from collections import Counter
from idlelib.iomenu import errors

import pandas as pd
from urllib3.util.util import to_str

from http_handler import http_handler


class data_handler:

    survey_url = "https://api.dawum.de/newest_surveys.json"

    def __init__(self, name):
        self.name = name

    @staticmethod
    def extract_mean_of_survey(self):

        get_handler = http_handler("get")

        umfrage_data = get_handler.get_request(self.survey_url)

        # results only relevant if Election is Bundestagswahl = "0"
        print(umfrage_data.get("Parliaments").get("0").get("Election"))

        # nur surveys werden extrahiert
        print(umfrage_data.get("Surveys").keys())
        survey_dict = umfrage_data.get("Surveys")

        # party keys werden in Liste umgewandelt
        party_dict_keys = list(umfrage_data.get("Parties").keys())
        party_anzahl = len(umfrage_data.get("Parties").keys())
        party_dict_keys.sort()
        print(party_dict_keys)

        # print names of parties if in survey / list of parties needs to be automated
        for p in range(0, party_anzahl - 1):
            if party_dict_keys[p] in ["1", "4", "7"]:
                print(umfrage_data.get("Parties").get(party_dict_keys[p]).get("Name"))

        # reading result dictionaries from umfrage JSON und errechne einen Durchschnitt
        i: int
        o: int
        bundestag_surveys = []
        umfrage_anzahl: int = len(umfrage_data.get("Surveys").keys())
        survey_dict_keys = list(umfrage_data.get("Surveys").keys())
        for i in range(0, umfrage_anzahl - 1):
            if umfrage_data.get("Surveys").get(survey_dict_keys[i]).get("Parliament_ID") == "0":
                print(survey_dict.get(survey_dict_keys[i]).get("Results"))
                #fügt alle aktuellen Umfragen als Dictionary in eine Liste
                bundestag_surveys.append(survey_dict.get(survey_dict_keys[i]).get("Results"))
                print(bundestag_surveys)
        # sum of surveys
        sum = bundestag_surveys
        c = Counter()
        for d in sum:
            c.update(d)
        print(c)

        # average of surveys with pandas
        df = pd.DataFrame(bundestag_surveys)

        answer = dict(df.mean())
        print(answer)

        #label columns with Party names
        k = df_columns_list = df.columns.to_list()
        print(df_columns_list[1])
        print(int(df_columns_list[3]))
        print(umfrage_data.get("Parties").get(df_columns_list[3]).get("Shortcut"))

        print(umfrage_data.get("Parties").get(party_dict_keys[1]).get("Name"))
        c: int
        for c in range(0,len(df_columns_list)):
            df.rename(columns={df_columns_list[c]:umfrage_data.get("Parties").get(df_columns_list[c]).get("Name")}, inplace=True)

        print(df)
        print(df.columns.values)
        print(answer)

        return df
    #add correct names of Parties to survey
    #def party_label(self,pd.DataFrame):


i = data_handler("mean")
i.extract_mean_of_survey