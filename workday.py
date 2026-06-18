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

role = "Data Science Analyst United States"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

# The body requires these parameters to handle pagination, filtering and search
payload = {
    "appliedFacets": {},
    "limit": 100,
    "offset": 0,
    "searchText": role,
}

job_filter = ["Just Posted", "Posted Today", "Posted Yesterday","Posted 2 Days Ago", 
              "Posted 3 Days Ago","Posted 4 Days Ago", "Posted 5 Days Ago"]

all_jobs = {}

for company in company_dict:
    print(company["company"], company["env"], company["user_name"])

    # The JSON search API lives at /wday/cxs/{tenant}/{site}/jobs — NOT the human-facing /en-US/ page URL
    url = f"https://{company['company']}.{company['env']}.myworkdayjobs.com/wday/cxs/{company['company']}/{company['user_name']}/jobs"

    # Number of jobs to return per page, offset for pagination, and search text are all passed in the body of the request
    off_set = 0

    while True:
        try:
            payload = {
                "appliedFacets": {},
                "limit": 20,
                "offset": off_set,
                "searchText": role,
            }
            
            response = requests.post(url, headers=headers, json=payload)

            if response.status_code == 200:
                data = response.json()

                job_data = data.get("jobPostings", [])

                filtered_jobs = [ job for job in job_data if job.get("postedOn") in job_filter ]

                if company["company"] not in all_jobs:
                    all_jobs[company["company"]] = []
                    all_jobs[company["company"]].append({"url": url})
                all_jobs[company["company"]].extend(filtered_jobs)

                off_set += 20  # Increment the offset for the next page of results

                if len(job_data) < 20:
                    break  # Exit the loop if there are no more jobs to fetch

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            break

with open("jobs.json", "w") as f:
    json.dump(all_jobs, f, indent=2)

print("Saved results to jobs.json")

