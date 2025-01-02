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
        print(umfrage_data["Surveys"])


        return umfrage_data



i = http_handler("dawum")
i.get_request()



