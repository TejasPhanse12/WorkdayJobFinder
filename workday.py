import requests
import json 

company_dict = [
    {"company":"comcast", "env":"wd5", "user_name":"Comcast_Careers"},
    {"company":"wexinc", "env":"wd5", "user_name":"WEXInc"},
    {"company":"idexx", "env":"wd1", "user_name":"IDEXX"},
    {"company":"abbott", "env":"wd5", "user_name":"abbottcareers"},
    {"company":"walmart", "env":"wd504", "user_name":"WalmartExternal"},
    {"company":"huron", "env":"wd1", "user_name":"huroncareers"},
    {"company":"nvidia", "env":"wd5", "user_name":"NVIDIAExternalCareerSite"},
]

role = "analyst"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

# The body requires these parameters to handle pagination, filtering and search
payload = {
    "appliedFacets": {},
    "limit": 20,
    "offset": 0,
    "searchText": role,
}

print(company_dict)

for company in company_dict:
    print(company["company"], company["env"], company["user_name"])
    # The JSON search API lives at /wday/cxs/{tenant}/{site}/jobs — NOT the human-facing /en-US/ page URL
    url = f"https://{company['company']}.{company['env']}.myworkdayjobs.com/wday/cxs/{company['company']}/{company['user_name']}/jobs"

    response = requests.post(url, headers=headers, json=payload)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        job_data = response.json()
        # This yields a beautifully structured list of open jobs
        print(json.dumps(job_data['jobPostings'], indent=2))

