from collections import Counter
import pandas as pd
from http_handler import http_handler


class data_handler:

    survey_url = "https://api.dawum.de/newest_surveys.json"

    def __init__(self, name):
        self.name = name

    @staticmethod
    def extract_institutes(self):

        get_handler = http_handler("getinstitute")

        institute_data = get_handler.get_request(self.survey_url)

        print(institute_data.get("Institutes"))
        print(len(list(institute_data.get("Institutes"))))

        #makes a list of keys
        x = list(institute_data.get("Institutes").keys())
        y = []
        print(x)
        print(y)
        
        #extracts names of the institutes and makes list out of it
        for l in range(0,len(list(institute_data.get("Institutes")))-1):
            y.append(institute_data.get("Institutes").get(x[l]).get("Name"))
            print(y)
        #creates a dictionary of x and y
        institute_dictionary = dict(zip(x,y))
        print(institute_dictionary)

    @staticmethod
    def extract_mean_of_survey(self):

        get_handler = http_handler("getmean")

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

               # reading result dictionaries from umfrage JSON and put all the results into a list of dictionaries
        i: int
        o: int
        bundestag_surveys = []
        bundestag_surveys_additional_info = []
        umfrage_anzahl: int = len(umfrage_data.get("Surveys").keys())
        survey_dict_keys = list(umfrage_data.get("Surveys").keys())
        for i in range(0, umfrage_anzahl - 1):
            if umfrage_data.get("Surveys").get(survey_dict_keys[i]).get("Parliament_ID") == "0":
                print(survey_dict.get(survey_dict_keys[i]).get("Results"))
                print(survey_dict.get(survey_dict_keys[i]).get("Date"))
                #fügt alle aktuellen Umfragen als Dictionary in eine Liste
                bundestag_surveys.append(survey_dict.get(survey_dict_keys[i]).get("Results"))
                #fügt das Institut, das Umfragedatum und die Umfragemethode in eine separate Liste
                bundestag_surveys_additional_info.append(survey_dict.get(survey_dict_keys[i]).get("Date"))
                print(bundestag_surveys)
                print(bundestag_surveys_additional_info)

        #add dates to data
        bundestag_surveys_date = dict(zip(bundestag_surveys_additional_info,bundestag_surveys))
        print(bundestag_surveys_date)
        df1 = pd.DataFrame(bundestag_surveys_date)

        #label lines with parties
        p = df1_line_list = df1.index.to_list()
        e: int
        for e in range (0,len(df1_line_list)):
            df1.rename(index={df1_line_list[e]:umfrage_data.get("Parties").get(df1_line_list[e]).get("Name")}, inplace=True)
        #convert columns to Datetime
        pd.to_datetime(df1.columns)
        df1 = df1.transpose()

        # average of surveys with pandas / The result list of JSON from Dawum is
        df = pd.DataFrame(bundestag_surveys)

        #answer ist das Mittel aller Abfragen
        answer = dict(df.mean())

        #label columns with Party names
        k = df_columns_list = df.columns.to_list()
        c: int
        for c in range(0,len(df_columns_list)):
            df.rename(columns={df_columns_list[c]:umfrage_data.get("Parties").get(df_columns_list[c]).get("Name")}, inplace=True)
        print(df1)
        print(df)
        print(df.columns.values)
        print(answer)
        #deletes the last survey because of being outdated
        df1.drop(df1.tail(3).index, inplace=True)
        print(df1)
        return df1


i = data_handler("mean")
i.extract_institutes(i)
i.extract_mean_of_survey(i)