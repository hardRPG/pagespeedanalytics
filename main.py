import os
import requests
import json
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

PSAPI_KEY = os.getenv("PAGESPEED_API_KEY")
testedURL = "https://jpw-development.de"
psBaseCall = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"

results = [
    {
        "URL": "https://example.com",
        "Performance": 91,
        "LCP": 1.8,
        "CLS": 0.03,
    },
    {
        "URL": "https://example2.com",
        "Performance": 76,
        "LCP": 2.9,
        "CLS": 0.1297897,
    },
]

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
        with open("analysen/json/pagespeed_response.json", "w", encoding="utf-8") as file:
            json.dump(response.json(), file, ensure_ascii=False, indent=2)
        df = pd.json_normalize(response.json())
        print(df)
        df.to_excel("analysen/excel/results.xlsx", index=False)
    elif 400 <= response.status_code < 500:
        print("Client error:", response.status_code, response.json())
    else: 
        print("Error:", response.status_code, response.text)



#df.to_excel("analysen/excel/results.xlsx", index=False)

callPagespeedAPI()
