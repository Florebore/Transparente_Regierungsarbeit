import json
import requests




class http_handler:

    url = "https://api.dawum.de/newest_surveys.json"

    def __init__(self, name):
        self.name = name



    def convert_json_to_ergebnisse(self, json):

        umfrage_dic = json

        return umfrage_dic


    def get_request(self):

        response = requests.get(self.url)
        umfrage_data = json.loads(response.text)
        print(type(umfrage_data))
        print(umfrage_data.keys())

        umfrage_anzahl = len(umfrage_data.get("Surveys").keys())
        print(umfrage_data.get("Parliaments").get("0").get("Election"))
        print(umfrage_data.get("Parties").keys())
        party_anzahl = len(umfrage_data.get("Parties").keys())
        print(party_anzahl)
        print(umfrage_data.get("Surveys").keys())
        survey_dict = umfrage_data.get("Surveys")
        survey_dict_keys = list(umfrage_data.get("Surveys").keys())
        print(survey_dict)
        i: int
        o: int

        for i in range(0,umfrage_anzahl-1):
            if umfrage_data.get("Surveys").get(survey_dict_keys[i]).get("Parliament_ID") == "0":
                print(survey_dict.get(survey_dict_keys[i]).get("Results"))


        return umfrage_data



i = http_handler("dawum")
i.get_request()



