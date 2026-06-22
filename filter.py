import requests
import json
import ollama


url = "https://abbott.wd5.myworkdayjobs.com/wday/cxs/abbott/abbottcareers/job/United-States---California---Alameda/Data-Science-and-Business-Analytics-Manager_31151998-1"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

response = requests.get(url, headers=headers)

print(response.status_code)

data = response.json()

print(json.dumps(data.get("jobPostingInfo", {}), indent=4))