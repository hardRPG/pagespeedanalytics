import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

PSAPI_KEY = os.getenv("PAGESPEED_API_KEY")
testedURL = "https://jpw-development.de"
psBaseCall = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"

params = {
    "key":PSAPI_KEY,
    "url":testedURL,
    "strategy":"MOBILE",
    "locale":"de-DE"
}

def callPagespeedAPI():
    response = requests.get(psBaseCall,params=params)
    if response.ok:
        #print("Response:", response.json())
        with open("analysen/pagespeed_response.json", "w", encoding="utf-8") as file:
            json.dump(response.json(), file, ensure_ascii=False, indent=2)
    elif 400 <= response.status_code < 500:
        print("Client error:", response.status_code, response.json())
    else: 
        print("Error:", response.status_code, response.text)


callPagespeedAPI()
