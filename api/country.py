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
            r = requests.get(url + dic["country"])
            data = r.json()
            if data:
                country_name = data[0]['name']['common']
                capital_name = data[0]['capital'][0] if 'capital' in data[0] else 'No Capital'
                message = f"The capital of {country_name} is {capital_name}."
            else:
                message = "No data found for the given country."
        else:
            message = "Please provide a valid country name."

        

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))
        return