from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):

        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        message = ""  # Initialize message variable

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
        elif "capital" in dic:
            url = "https://restcountries.com/v3.1/capital/"
            r = requests.get(url + dic["capital"])
            data = r.json()
            if data:
                country_name = data[0]['name']['common']
                capital_name = data[0]['capital'][0] if 'capital' in data[0] else 'No Capital'
                message = f"{capital_name} is the capital of {country_name}."
            else:
                message = "No data found for the given capital."
        else:
            message = "Please provide a valid country name or capital name."

        # Send the response
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())
