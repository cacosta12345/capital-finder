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
            r= requests.get(url + dic["word"])
            data = r.json()
            country_info = []
            for word_data in data:
                capital_data = word_data["capital"][0]
                country_info.append(capital_data)
            message = str(country_info)

        else:
            message = "Please provide valid country"

        

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))
        return