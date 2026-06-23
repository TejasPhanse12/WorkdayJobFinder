# WorkdayJobFinder

WorkdayJobFinder is an automated tool designed to help students and job seekers efficiently search for job opportunities across multiple companies that host their career portals on the Workday platform. Instead of visiting each company's site individually, this tool queries their APIs, filters jobs by post recency, and extracts detailed descriptions to compile a clean, unified report.

---

## Codebase Architecture & File Structure

The project has been refactored to decouple configuration, search logic, and detail-filtering logic. Here is how the files interact:

```
                  ┌──────────────────────┐
                  │   companyinfo.py     │ <─── Holds target role & company lists
                  └──────────┬───────────┘
                             │
            ┌────────────────┴────────────────┐
            ▼                                 ▼
    ┌──────────────┐                  ┌──────────────┐
    │  workday.py  │                  │  filter.py   │
    └──────┬───────┘                  └──────┬───────┘
           │ (Queries Workday API            │ (Reads metadata & fetches
           │  for match list)                 │  full job descriptions)
           ▼                                 ▼
    ┌──────────────┐                  ┌──────────────┐
    │  jobs.json   │ ────────────────> │  output.txt  │
    └──────────────┘                  └──────────────┘
 (Intermediate metadata)           (Final readable report)
```

- **`companyinfo.py`**: The configuration hub. Contains the `CompanyInfo` class which defines the target job `role` and the list of companies (`company_dict`) to search.
- **`workday.py`**: The search orchestrator. Queries the search endpoint of each configured company's Workday portal for jobs matching the target role, filters them by recency, and outputs metadata to `jobs.json`.
- **`filter.py`**: The scraper and formatter. Reads the matched job postings from `jobs.json`, fetches the complete details (including full descriptions and locations) for each listing, and outputs a formatted report to `output.txt`.
- **`jobs.json`**: Intermediate JSON storage containing matching job metadata.
- **`output.txt`**: The final, human-readable report listing all identified jobs with their titles, locations, posting dates, and detailed descriptions.

---

## Prerequisites

- **Python 3.x**
- **`requests` library**

Install the required library with:
```bash
pip install requests
```

---

## Configuration

All search settings and targets are configured in `companyinfo.py`.

### 1. Setting the Target Role
Update the `role` class variable inside `companyinfo.py` with the exact keywords or job titles you are looking for:
```python
role = "Data Science Analyst United States"
```

### 2. Managing Companies (`company_dict`)
The `company_dict` list is a collection of dictionaries mapping out active Workday career portals. Each dictionary has three key fields:

| Key | Description | Example |
| :--- | :--- | :--- |
| `company` | The primary name of the company (subdomain on Workday). | `comcast`, `nvidia` |
| `env` | The specific Workday environment/instance (e.g., `wd1`, `wd5`). | `wd5` |
| `user_name` | The company's unique site or career-portal identifier slug. | `Comcast_Careers` |

Example entry in `companyinfo.py`:
```python
{"company": "nvidia", "env": "wd5", "user_name": "NVIDIAExternalCareerSite"}
```

---

## Usage

Running the job search is a simple two-step process:

### Step 1: Query Workday and Save Matches
Run `workday.py` to search for jobs matching your target role across all configured companies. This script queries the APIs, applies a recency filter (e.g., jobs posted within the last 5 days), and saves the basic results to `jobs.json`.

```bash
python workday.py
```

### Step 2: Extract Full Details
Run `filter.py` to process the intermediate `jobs.json` file. This script fetches the complete description, exact location, and detailed info for each match, saving the finalized report into `output.txt`.

```bash
python filter.py
```

After step 2, open `output.txt` to view your compiled list of tailored job postings!

---

## Project Status & Roadmap

- [x] Automate the extraction of job listings and display them in a unified format.
- [x] Export results to a JSON file (`jobs.json`) and final text output (`output.txt`).
- [ ] Add support for filtering by location.
- [ ] Implement a command-line interface (CLI) for managing roles and companies dynamically.
