import requests
import json 

company_dict = [
    {"company":"comcast", "env":"wd5", "user_name":"Comcast_Careers"},
    {"company":"wexinc", "env":"wd5", "user_name":"WEXInc"},
    {"company":"idexx", "env":"wd1", "user_name":"IDEXX"},
    {"company":"abbott", "env":"wd5", "user_name":"abbottcareers"},
    {"company":"walmart", "env":"wd504", "user_name":"WalmartExternal"},
    {"company":"huron", "env":"wd1", "user_name":"huroncareers"}
]

role = "analyst"

print(company_dict)

for company in company_dict:
    print(company["company"])
    url = f"https://{company["company"]}.{company["env"]}.myworkdayjobs.com/en-US/{company["user_name"]}?q={role}"

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }