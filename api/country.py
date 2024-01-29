from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):

        s= self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if "country" in dic:
            url = "https://restcountries.com/v3.1/name/"
            r= requests.get(url + dic["country"])
            data = r.json()
            country_capital = []
            country_name = []
            for word_data in data:
                country_name_data = word_data[0]["name"][0]["common"][0]
                capital_data = word_data["capital"][0]
                country_name.append(country_name_data)
                country_capital.append(capital_data)
            message = f"The capital of {str(country_name) is {str(country_capital)}}"

        else:
            message = "Please provide valid country"

        

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))
        return