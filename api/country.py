from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):

        s= self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        url = "https://restcountries.com/v3.1/"

        if "country" in dic:
            endpoint = url+"name/" + dic["country"]
            r = requests.get(endpoint)
            data = r.json()
            if data:
                country_name = data[0]['name']['common']
                capital_name = data[0]['capital'][0] if 'capital' in data[0] else 'No Capital'
                message = f"The capital of {country_name} is {capital_name}."
            else:
                message = "Error getting country info."
       
        elif "capital" in dic:
            endpoint = url+"capital/" + dic["capital"]
            r = requests.get(endpoint)
            data = r.json()
            if data:
                country_name = data[0]['name']['common']
                capital_name = data[0]['capital'][0] if 'capital' in data[0] else 'No Capital'
                message = f"{capital_name} is the capital of {country_name}."
            else:
                message = "Error getting capital info."

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))
        return