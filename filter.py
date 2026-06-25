import requests
import json
import companyinfo as cpi
import ollama 

model = ollama.Client(model="llama3.2:3b")

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

company_dict = cpi.CompanyInfo("comcast", "wd5", "Comcast_Careers").get_company_info()
jobs = json.load(open("jobs.json", "r"))

with open("output.txt", "w") as out:
    for company in company_dict:
        company_jobs = jobs.get(company["company"], [])

        # Skip URL stub entries (artifacts from workday.py) — only keep real job entries
        job_entries = [j for j in company_jobs if "externalPath" in j]

        if not job_entries:
            out.write(f"No jobs found for {company['company']}. Skipping...\n")
            out.write("-" * 60 + "\n")
            continue

        for job in job_entries:
            external_path = job["externalPath"]

            url = f"https://{company['company']}.{company['env']}.myworkdayjobs.com/wday/cxs/{company['company']}/{company['user_name']}{external_path}"

            out.write(f"\nFetching: {job.get('title', 'Unknown')} @ {company['company']}\n")

            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()
                job_info = data.get("jobPostingInfo", {})
                description = job_info.get("jobDescription", "No description available")
                out.write(f"Location : {job.get('locationsText', 'N/A')}\n")
                out.write(f"Posted   : {job.get('postedOn', 'N/A')}\n")
                out.write(f"Description:\n{description}\n")
                out.write("-" * 60 + "\n")
            else:
                out.write(f"  Failed ({response.status_code}) — skipping\n")
